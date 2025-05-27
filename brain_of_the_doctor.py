# # if you dont use pipenv uncomment the following:
# # from dotenv import load_dotenv
# # load_dotenv()

# #Step1: Setup GROQ API key
# import os
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))



# #Step2: Convert image to required format
# import base64


# #image_path="acne.jpg"

# def encode_image(image_path):   
#     image_file=open(image_path, "rb")
#     return base64.b64encode(image_file.read()).decode('utf-8')

# #Step3: Setup Multimodal LLM 
# from groq import Groq

# query="Is there something wrong with my face?"
# model = "meta-llama/llama-4-scout-17b-16e-instruct"
# #model="llama-3.2-90b-vision-preview" #Deprecated

# def analyze_image_with_query(query, model, encoded_image):
#     client=Groq()  
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text", 
#                     "text": query
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/jpeg;base64,{encoded_image}",
#                     },
#                 },
#             ],
#         }]
#     chat_completion=client.chat.completions.create(
#         messages=messages,
#         model=model
#     )

#     return chat_completion.choices[0].message.content





from groq import Groq
import os
import base64

def encode_image(image_path):   
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def analyze_image_with_query(query, model, encoded_image):
    # ✅ Correct client initialization with API key
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    messages = [
    {
        "role": "user",
        "content": query
    }
]


    chat_completion = client.chat.completions.create(
        messages=messages,
        model = "llama3-8b-8192"  # ✅ Groq supported model

    )

    return chat_completion.choices[0].message.content


