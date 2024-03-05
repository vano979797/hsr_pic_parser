diff --git a/README.md b/README.md
index a39191b..9ad8e93 100644
--- a/README.md
+++ b/README.md
@@ -2,25 +2,26 @@
 
 ## Introduction
 
-This is a Python library for getting pictures of characters, cones and relics with names from [starrail.mana](https://starrail.mana.wiki/).
+This is a Python library for getting pictures of characters, light cones, relics and planetaries with names from [starrail.mana](https://starrail.mana.wiki/).
 
 
 ## Installation
 
-pip install hsr_pic_parser
-
+```python
+pip install hsr-pic-parcer
+```
 
-##Functions, which can be used
+## Available functionality
 
 ```python
-get_char_pic(name) # returns bynary picture of the character and full name of the character
-get_char_icon_pic(name)) # returns bynary icon picture of the character and full name of the character
-get_cone_pic(number) # returns bynary icon picture of the cone and full name of cone
-get_cone_icon_pic(number) # returns bynary icon picture of the cone and full name of cone
-get_relic_icon_pic(number) # returns bynary icon picture of the relic and full name
+get_char_pic(name) # returns binary picture of the character and full name of the character
+get_char_icon_pic(name) # returns binary icon picture of the character and full name of the character
+get_cone_pic(number) # returns binary picture of the light cone and full name of the light cone
+get_cone_icon_pic(number) # returns binary icon picture of the light cone and full name of the light cone
+get_relic_icon_pic(number) # returns binary icon picture of the relic or planetary and full name of the relic or planetary
 ```
 
-## Example
+## Examples
 
 You can get picture of character using the following code:
 
@@ -29,7 +30,7 @@ from hsr_pic_parser import get_char_pic
 
 picture, name = get_char_pic('argenti')
 ```
-The name of the character should be identical to the one used in [starrail.mana](https://starrail.mana.wiki/).
+The name of the character should be identical to the one used on [starrail.mana](https://starrail.mana.wiki/).
 
 You can get picture and the name of the light cone:
 
@@ -38,19 +39,16 @@ from hsr_pic_parser import get_cone_pic
 
 picture, name = get_cone_pic(20000)
 ```
-The code of the light cone should be equivalent to the one used in [starrail.mana](https://starrail.mana.wiki/).
+The code of the light cone should be equivalent to the one used on [starrail.mana](https://starrail.mana.wiki/).
 
-## Another example
 ```python
 from hsr_pic_parser import get_relic_icon_pic
 
-pic, name = get_relic_icon_pic(101) #here we are using function
+picture, name = get_relic_icon_pic(101)
 
 def save_image_as_png(image_data, output_file_path):
     with open(output_file_path, "wb") as png_file:
-        png_file.write(image_data) #here is saving function 
+        png_file.write(image_data)
 
-save_image_as_png(pic, argenty) #here we are saving the icon of relic
+save_image_as_png(picture, f"${name}.png")
 ```
