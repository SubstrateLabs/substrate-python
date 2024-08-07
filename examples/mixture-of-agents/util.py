import os

sample_question = "What was Arendt's notion of Freedom? How did she distinguish it from Action?"

aggregate = """You have been provided with a set of responses from various open-source models to the latest user query. Your task is to synthesize these responses into a single, high-quality response. It is crucial to critically evaluate the information provided in these responses, recognizing that some of it may be biased or incorrect. Your response should not simply replicate the given answers but should offer a refined, accurate, and comprehensive reply to the instruction. Ensure your response is well-structured, well-considered, and adheres to the highest standards of accuracy and reliability. Do not respond as if we're having a conversation, just output an objective response."""

jq_list = 'to_entries | map(((.key + 1) | tostring) + ". " + .value) | join("\n")'

current_dir = os.path.dirname(os.path.abspath(__file__))
