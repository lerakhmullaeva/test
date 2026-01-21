# adwentures_of_tom_sawer = """\
# Tom gave up the brush with reluctance in his .... face but alacrity
# in his heart. And while
# the late steamer
# "Big Missouri" worked ....
# and sweated
# in the sun,
# the retired artist sat on a barrel in the .... shade close by, dangled his legs,
# munched his apple, and planned the slaughter of more innocents.
# There was no lack of material;
# boys happened along every little while;
# they came to jeer, but .... remained to whitewash. ....
# By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
# a kite, in good repair;
# and when he played
# out, Johnny Miller bought
# in for a dead rat and a string to swing it with—and so on, and so on,
# hour after hour. And when the middle of the afternoon came, from being a
# poor poverty, stricken boy in the .... morning, Tom was literally
# rolling in wealth."""

# ##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# # task 01 ==
# """ Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
# треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

fixed = adwentures_of_tom_sawer.replace("\n", " ")

# # task 02 ==
# """ Замініть .... на пробіл """
fixed1 = fixed.replace("....", " ")
print(fixed1)

# # task 03 ==
# """ Зробіть так, щоб у тексті було не більше одного пробілу між словами."""
space1= " ".join(
    fixed1.split()
)
print(space1)

# # task 04
# """ Виведіть, скількі разів у тексті зустрічається літера "h""""
search_h = space1.count("h")
if search_h != -1:
    print(f"Found {search_h}.")
else:
    print("Not found")

# # task 05
# """ Виведіть, скільки слів у тексті починається з Великої літери?"""
upper = space1.split()
count_upper = 0
for word in upper:
    clean = word.lstrip("\"'—-()")  # прибрати зайві символи спереду
    if clean and clean[0].isupper():
        count_upper += 1
print(count_upper)

# # task 06
# """ Виведіть позицію, на якій слово Tom зустрічається вдруге """
find_first_Tom = space1.find("Tom")
print(find_first_Tom)
find_second_Tom = space1.find("Tom", find_first_Tom +1)
print(find_second_Tom)
# find_third_Tom = space1.find("Tom", find_second_Tom +1)
# find_fourth_Tom = space1.find("Tom", find_third_Tom +1)  /приклад джаст фор майселф
# if find_fourth_Tom == -1:
#     print("Word does not appear fourth time")

# # task 07
# """ Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
# Збережіть результат у змінній adwentures_of_tom_sawer_sentences """
adwentures_of_tom_sawer_sentences = space1.split('. ')
print(adwentures_of_tom_sawer_sentences)

# # task 08
# """ Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
# Перетворіть рядок у нижній регістр. """
fourth_sentence = adwentures_of_tom_sawer_sentences[3]
fourth_sentence_lowercase = fourth_sentence.lower()
print(fourth_sentence_lowercase)

# # task 09
# """ Перевірте чи починається якесь речення з "By the time". """
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        print("Yes, there's a sentence that starts with 'By the time")
    else:
        print("Yes, there's a sentence that starts with 'By the time'")
    # if sentence.strip().startswith("By the night"):
    #     print("Yes, there's a sentence that starts with 'By the night'")   /приклад джаст фор майселф
    # else:
    #     print("There are no matches")

# # task 10
# """ Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences. """
last_sentence = adwentures_of_tom_sawer_sentences[-1]
words = last_sentence.split()
word_count = len(words)
print(word_count)