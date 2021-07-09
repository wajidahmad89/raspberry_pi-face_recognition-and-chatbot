


import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from keras.models import load_model

model = load_model('chatbot_model.h5')
import json
import random

intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

    # return bag of words array: 0 or 1 for each word in the bag that exists in the sentence


def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return (np.array(bag))


def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if (i['tag'] == tag):
            result = random.choice(i['responses'])
            break
    return result


def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res

    # Read User Response - copied from last_line-to-tk




###################
###################
###################
###################
###################




#####       initiation_process          #####
#####       without this , the          #####
#####       initial response time       #####
#####       is long                     #####

#def rpapp_main():

msg_initiate = "Start initiation"

text_file = open("botresponse.txt", "w")
text_file.write(chatbot_response(msg_initiate))
text_file.close()


###########################################




while True:
    with open('hello_camera-output.txt') as f:
        num_lines = sum(1 for line in f)
        if num_lines >= 3:
                #####       say-hello       #####
            
            
            import os

            os.system("espeak -f hello_camera-output.txt --stdout |aplay")
            
            with open('userinput.txt', 'w') as g:
                g.write("null")
            ####################################################################################

            #####       speech-to-text      #####
            
            
            import speech_recognition as sr
            import os
            import wave
            
            
            while True:
                r = sr.Recognizer()


                ###     THIS IS FOR MY MIC      ###
                os.system("arecord -D plughw:1,0 -d 5 the_audio.wav")
                ###################################


                the_audio = sr.AudioFile("the_audio.wav")
                
                
                with the_audio as source:
                    r.adjust_for_ambient_noise(source)
                    the_audio_audio = r.record(source)
                    
                    text_file = open("userinput.txt", "a")
                    text_file.write("\n")
                    
                    try:
                        text_file.write(r.recognize_google(audio_data=the_audio_audio))

                    except:
                        text_file.write("\n")


                    text_file.close()
                
                
                
                
                
                #####       goodbye + person_name     #####

                user_file = open('userinput.txt', 'r')
                user_lines = user_file.read().splitlines()
                user_last_line = user_lines[-1]
                user_file.close()

                if len(user_last_line.strip()) == 0:
                    
                    import os

                    os.system("espeak -f goodbye_camera-output.txt --stdout |aplay")
                    
                    
                    break



                #####       botresponse     #####
                
                
                #####       response_process        #####


                with open('userinput.txt', 'r') as f:
                    lines = f.read().splitlines()
                    msg = lines[-1]



                text_file = open("botresponse.txt", "w")
                text_file.write(chatbot_response(msg))
                text_file.close()



                #####       speak the response_process        #####

                import os

                os.system("espeak -f botresponse.txt --stdout |aplay")
                
                
                
                

            
            break
            
            

