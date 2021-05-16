from ChatBot import *

training_list = []
with open("E:\\AI and ML\\WikiQACorpus\\WikiQA-train.txt", encoding="utf8") as file:
    for line in file:
        input_split = line.split("\t")
        training_list.append(input_split[0])
        training_list.append(input_split[1])

chat_bot_trainer.train(training_list)

training_list = []
with open("E:\\AI and ML\\Chat bot training\\S08\\question_answer_pairs.txt", encoding="utf8") as file:
    for line in file:
        input_split = line.split("\t")
        training_list.append(input_split[1])
        training_list.append(input_split[2])

chat_bot_trainer.train(training_list)

training_list = []
with open("E:\\AI and ML\\Chat bot training\\S09\\question_answer_pairs.txt", encoding="utf8") as file:
    for line in file:
        input_split = line.split("\t")
        training_list.append(input_split[1])
        training_list.append(input_split[2])

chat_bot_trainer.train(training_list)

training_list = []
with open("E:\\AI and ML\\Chat bot training\\S10\\question_answer_pairs.txt", encoding="utf8") as file:
    for line in file:
        input_split = line.split("\t")
        training_list.append(input_split[1])
        training_list.append(input_split[2])

chat_bot_trainer.train(training_list)
