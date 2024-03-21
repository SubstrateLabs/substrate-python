import logging
import datetime
import platform
from typing import Any, Dict, Union, Optional
from typing_extensions import Literal

import httpx
import distro

from ._version import __version__

log: logging.Logger = logging.getLogger(__name__)


class OtherPlatform:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Other:{self.name}"


Platform = Union[
    OtherPlatform,
    Literal[
        "MacOS",
        "Linux",
        "Windows",
        "FreeBSD",
        "OpenBSD",
        "iOS",
        "Android",
        "Unknown",
    ],
]


class OtherArch:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"other:{self.name}"


Arch = Union[OtherArch, Literal["x32", "x64", "arm", "arm64", "unknown"]]


def get_platform() -> Platform:
    system = platform.system().lower()
    platform_name = platform.platform().lower()
    if "iphone" in platform_name or "ipad" in platform_name:
        return "iOS"
    if system == "darwin":
        return "MacOS"
    if system == "windows":
        return "Windows"
    if "android" in platform_name:
        return "Android"
    if system == "linux":
        distro_id = distro.id()
        if distro_id == "freebsd":
            return "FreeBSD"
        if distro_id == "openbsd":
            return "OpenBSD"
        return "Linux"
    if platform_name:
        return OtherPlatform(platform_name)
    return "Unknown"


def get_architecture() -> Arch:
    python_bitness, _ = platform.architecture()
    machine = platform.machine().lower()
    if machine in ("arm64", "aarch64"):
        return "arm64"
    if machine == "arm":
        return "arm"
    if machine == "x86_64":
        return "x64"
    if python_bitness == "32bit":
        return "x32"
    if machine:
        return OtherArch(machine)
    return "unknown"


class APIResponse:
    http_response: httpx.Response
    _json: Optional[Dict[str, Any]]

    def __init__(self, http_response: httpx.Response):
        self.http_response = http_response
        self._json = None
        try:
            self._json = self.http_response.json()
        except Exception as exc:
            log.debug("Could not read JSON from response data due to %s - %s", type(exc), exc)

    @property
    def json(self) -> Optional[Dict[str, Any]]:
        return self._json

    @property
    def headers(self) -> httpx.Headers:
        return self.http_response.headers

    @property
    def http_request(self) -> httpx.Request:
        return self.http_response.request

    @property
    def status_code(self) -> int:
        return self.http_response.status_code

    @property
    def url(self) -> httpx.URL:
        return self.http_response.url

    @property
    def method(self) -> str:
        return str(self.http_request.method)

    @property
    def content(self) -> bytes:
        return self.http_response.content

    @property
    def text(self) -> str:
        return self.http_response.text

    @property
    def http_version(self) -> str:
        return self.http_response.http_version

    @property
    def elapsed(self) -> datetime.timedelta:
        """The time taken for the complete request/response cycle to complete."""
        return self.http_response.elapsed


class APIClient:
    api_key: str
    base_url: str
    _client: httpx.Client
    _async_client: httpx.AsyncClient
    _version: str

    def __init__(
        self,
        api_key: str,
        base_url: str,
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url
        timeout = httpx.Timeout(60.0)  # default is 5s
        self._client = httpx.Client(timeout=timeout)
        self._async_client = httpx.AsyncClient(timeout=timeout)
        self._version = __version__

    @property
    def user_agent(self) -> str:
        return f"{self.__class__.__name__}/Python {self._version}"

    @property
    def auth_headers(self) -> Dict[str, str]:
        return {"Authorization": f"Bearer {self.api_key}"}

    @property
    def platform_headers(self) -> Dict[str, str]:
        version_parts = self._version.split(".")
        date = version_parts[0][-8:]
        api_version = f"{date[:4]}-{date[4:6]}-{date[6:]}"
        return {
            "X-Substrate-Lang": "python",
            "X-Substrate-Package-Version": self._version,
            "X-Substrate-Version": api_version,
            "X-Substrate-OS": str(get_platform()),
            "X-Substrate-Arch": str(get_architecture()),
            "X-Substrate-Runtime": platform.python_implementation(),
            "X-Substrate-Runtime-Version": platform.python_version(),
        }

    @property
    def default_headers(self) -> Dict[str, str]:
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": self.user_agent,
            **self.platform_headers,
            **self.auth_headers,
        }

    def post_compose(self, dag: Dict[str, Any]) -> APIResponse:
        url = f"{self.base_url}/compose"
        body = {"dag": dag}
        http_response = self._client.post(url, headers=self.default_headers, json=body)
        res = APIResponse(http_response=http_response)
        return res

    async def async_post_compose(self, dag: Dict[str, Any]) -> APIResponse:
        url = f"{self.base_url}/compose"
        body = {"dag": dag}
        http_response = await self._async_client.post(url, headers=self.default_headers, json=body)
        return APIResponse(http_response=http_response)
