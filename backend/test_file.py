import openai 
from dotenv import load_dotenv

load_dotenv()

prompt = """Generate dynamic and engaging Brazilian Jiu-Jitsu training videos with the following details:

- Belt Level: [Specify the belt level]
- Techniques Focus: [Specify the main techniques]
- Duration: [Specify the duration of the training]
- Additional Preferences: [Any other specific preferences]

Job Description:
Proven experience as a Brazilian Jiu-Jitsu instructor or similar role
In-depth knowledge of BJJ techniques, strategies, and training methodologies
Strong communication skills to effectively convey instructions
Ability to create engaging and informative training sessions

Response: 
"""

response = openai.Completion.create(
    engine="davinci-codex",
    prompt=prompt,
    max_tokens=700,
    temperature=0.7
)

# Process the response as needed
video_scenario = response['choices'][0]['text']
# 'video_scenario' to create the actual video content
