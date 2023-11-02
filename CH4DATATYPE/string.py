name = "Kolawole Ayodeji"
age = "24"
age2 = 24
print(type(name))
print(type(age))
print(type(age2))

# Multi-line String

multi_line_str = "Never gone gonna give you up\
        Never gonna let you down\
        Never gonna leave you\
        "
print(multi_line_str)


# Doc string documentation: Good for documenting functions, classes etc
twinkle = """
    Twinkle Twinkle Little Star
    How I wonder what you are
"""
print(twinkle)


"""
Accessing string indices/Index
"""
tea = "Tea"
print(tea[0])
print(tea[1])
print(tea[2])

"""
Accessing Negative Indices
"""
print("........................................................")
print(tea[-1])
print(tea[-2])
print(tea[-3])


"""
String Membership
"""
print("e" in tea)
print("q" in tea)

"""
String Comparison
"""
tea2 = "tea"

print(tea == tea2)

"""
    Escape Character
"""
sentence1 = "He said, \"Better call Saul\" "
sentence2 = "He said, 'Better call Saul'"

print(sentence1)
print(sentence2)

word = "Sentence\\"
print(word)


"""
Basic Escape Character
"""

long_sentence = 'Lorem ipsum dolor sit amet consectetur \nadipisicing elit. Itaque architecto amet ad beatae, qui neque doloribus adipisci quis a earum perspiciatis eligendi pariatur magnam \nvoluptatibus rem id placeat consequatur laudantium sequi. Esse cum vel repudiandae pariatur aut error inventore facere quod accusamus \nlaboriosam minima delectus corrupti optio, voluptas accusantium, qui quia! Quia consequuntur iusto corrupti, doloremque fugit ab sint impedit ea recusandae \nperspiciatis quis enim quisquam accusamus blanditiis repellat nobis. Recusandae repellat repudiandae amet, nostrum fugit porro enim est itaque \naperiam! Beatae rerum nihil doloribus blanditiis quibusdam veniam tempore, officiis, quasi error voluptas modi nisi tempora totam eos incidunt \tcorporis quas sunt? Illum nostrum nobis a quis aspernatur perferendis iure fugit voluptas id, aliquam impedit autem ad ut dolore blanditiis quos minus enim nihil aperiam voluptates provident? Quas illo nulla ipsa necessitatibus earum perspiciatis. \tReiciendis eligendi dolorum autem maiores assumenda, ipsa dolorem incidunt, eos qui fugit tenetur sint molestias, explicabo voluptatum voluptate iusto quasi consectetur est consequuntur minima! \nDolore voluptatum quo sapiente libero provident assumenda cum sit? Quibusdam, amet quis debitis ullam, pariatur fuga, minus esse \nveritatis molestias quod suscipit autem eaque sapiente dolorum officiis odit modi consectetur fugit. Aliquid mollitia sapiente necessitatibus, \nratione eligendi perferendis repellat veniam iure libero.'

print(long_sentence)

"""
    String Method
"""
print(sentence1.upper())
