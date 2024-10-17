#Copyright 2024 Google LLC
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#    https://www.apache.org/licenses/LICENSE-2.0
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
imageprompt = """
General Information
What objects are present in the image? (Identify the main objects and their categories)
What is the overall scene depicted in the image? (Describe the environment and context)
Are there any people in the image? If so, who are they and what are they doing? (Identify individuals, their actions, and potential relationships)
What is the emotional impact of the image? (Analyze the mood, tone, and feelings evoked)
What are the dominant colors in the image and what is their effect? (Analyze the color palette and its influence on the overall impression)
Composition and Technique
How is the image composed? (Analyze the arrangement of elements, leading lines, and visual balance)
What photographic or artistic techniques are used? (Identify techniques like lighting, perspective, depth of field, etc.)
Is there any text in the image? What does it say? (Extract and analyze any text present)
What is the resolution and aspect ratio of the image? (Get technical details about the image dimensions)
What is the potential story behind the image? (Encourage narrative interpretation)
What is the cultural or historical context of the image? (Analyze potential influences and references)
What symbols or metaphors are present? (Identify and interpret symbolic elements)
What message or idea is the image trying to convey? (Analyze the intended communication)
How does this image compare to others in a similar category or style? (Draw comparisons and analyze differences)
Image Quality
Is the image clear or blurry? (Assess the overall image quality)
These questions can be adapted and expanded upon depending on the specific focus of your image analysis application. You can also combine them with user-provided information or context to generate even more insightful analysis.
"""

image_analysis_output = """
Output is markdown. 
Return multiple markdown tables of analysis, 
separate each table by an h4 sized header explaining what the data is, 
provide a summary text at the end with your reasoning.  
Example Output:
A table with metadata from the receipt, the McDonald's store information. key/value. date, time, order number, address.
A table with the breakdown of the Order information from the receipt. qty, name, NO, ADD.
A table of data analyzing the food from the picture. Item, toppings included, toppings missing.
Summary: written explanation of pass/fail, be verbose, use all data from the receipt and image for your justification.  
If multiple issues are present be sure to talk to them.
Do not use <br> HTML in your response, if you need to separate data just use a comma.      
"""


markdown_testing = """
#### General Information

| Attribute | Value |
|---|---|
| Objects |  McDouble (hamburger), French Fries, McDonald's wrapper, Receipt, Sprite  |
| Scene |  A McDonald's meal laid out on a McDonald's wrapper.  |
| People |  No  |
| Emotional Impact |  Craving for fast food, perhaps a sense of indulgence or guilty pleasure.  |
| Dominant Colors |  Red, Yellow, Brown. The colors are typical of the McDonald's brand and evoke feelings of hunger and familiarity. |

#### Composition and Technique

| Attribute | Value |
|---|---|
| Composition |  The image is a relatively straightforward snapshot, likely taken from above. The food and receipt are the main focus. |
| Techniques |  Natural lighting, close-up shot  |
| Text Present? |  Yes, the receipt contains order information and details about a customer satisfaction survey.  |
| Resolution |  Unknown  |
| Aspect Ratio |  Unknown  |
| Potential Story | The image might depict a typical fast-food meal, possibly purchased by someone on the go. The inclusion of the receipt suggests a documentation of the purchase.  |
| Cultural Context |  The image represents a snapshot of fast food culture, particularly in America, where McDonald's is a ubiquitous brand.  |
| Symbols |  The McDonald's logo and the food items themselves are symbolic of fast food consumption and its associated connotations (convenience, affordability, etc.). |
| Message |  The image doesn't convey a strong message beyond documenting a McDonald's meal. It might subtly reinforce the normalcy of fast food consumption. |
| Comparison to similar images | This image is very typical of countless other images depicting fast food meals. The presence of the receipt adds a slight element of uniqueness.  |

#### Image Quality

| Attribute | Value |
|---|---|
| Clarity |  The image is reasonably clear and adequately lit, allowing for easy identification of the objects and text. |

#### Summary

The image shows a standard McDonald's meal, with a McDouble, french fries and a Sprite.  The receipt shows a request for no mustard and no pickle, but added mayonnaise. The picture does not show a detailed view of the burger, but it does show ketchup, so we don't know for sure if the customer got what they ordered.   
"""