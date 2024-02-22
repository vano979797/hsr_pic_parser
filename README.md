# hsr_pic_parser

## Introduction

This is a Python library for getting pictures of characters, cones and relics with names from [starrail.mana](https://starrail.mana.wiki/).


## Example

You can get picture of character using the following code:

```python
from hsr_pic_parser import get_char_pic

picture, name = get_char_pic('argenti')
```
The name of the character should be identical to the one used in [starrail.mana](https://starrail.mana.wiki/).

You can get picture and the name of the light cone:

```python
from hsr_pic_parser import get_cone_pic

picture, name = get_cone_pic(20000)
```
The code of the light cone should be equivalent to the one used in [starrail.mana](https://starrail.mana.wiki/).

## Installation

Will be soon
