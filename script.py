import os
import re
import shutil
import glob
import re
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import codecs
from googletrans import Translator
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
def replace_quotes(e):
        translated = GoogleTranslator(source='auto', target='hindi').translate(e)
        # translator = Translator(service_urls=['translate.google.com'])
        # translator.raise_Exception = True
        # # print(e)
        # translated_text = translator.translate(e,dest='hi',src='en').text
        # # print("--------------------------------------------")
        return  translated
    
def translate_html(html_directory):
    with codecs.open(html_directory, 'r', 'utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    translated=[]
    origin=[]
    print('Translating....')
            
    for e in (soup.stripped_strings):
        e = e.replace('.', '. ')
        if e == "\n":
            continue
        if e=='' or e=='.' or e=='•' or e=='. ' or e==":" or e=="/" or e=='!' or e==')' or e=='(' or e=='|':
            continue 
        try:
            new=replace_quotes(e)
        except:
            print(e,"errrrrrrrrrrrr")
            continue
        origin.append(e)
        translated.append(new)

    # for e,i in zip(origin,translated):
    #     print(e,i)
    #     print('------------------------------------------')
    with codecs.open(html_directory, 'r', 'utf-8') as f:
        html = f.read()
    u=0
    # print(len(translated))
    new = BeautifulSoup(html, 'html.parser')
    soup = BeautifulSoup(html, 'html.parser')
    # comments=[]
    mashakel=[]
    for script in new(["script", "style"]):                   
        script.decompose() 
    t=0
    def return_comment(comment,f):
        if comment == None:
            return ''
        if comment not in f:
            return '' 
        elif comment in soup(['style', 'script']):
            return '' 
        elif comment.find_parent("style"):
            return '' 
        elif comment.find_parent("script"):
            return '' 
        else:
            return comment
    def replace_kamek(comment,e,i):
        print(e,i,"ooooooooooooooooooo")
        fixed_text = comment.replace(e, i)
        comment.replace_with(fixed_text)
        return comment

    def replace_kamek2(comment,e,i):
        # print(e,i)
        fixed_text = comment.replace(e, i)
        comment.string.replace_with(fixed_text)
        return comment

    def replace_and_create_file(html):
        with open(html,'w', encoding='utf-8') as infile:
        # infile.write(str(soup))  
            infile.write(soup.prettify())
    print("Replacing")
    for e,i in zip(origin,translated):
        # print(e,i)
    ###################################3 tmmm m3ada sign upp
        # comment = soup.find(string=re.compile(e))
        # f = new.find_all(string=re.compile(e))
    
        # comment = return_comment(comment,f)
        # if comment=='':
        #     continue
        # comment = replace_kamek2(comment,e,i)
    ##################################3###   shwya
        # comment = soup.find(string=e)
        # f = new.find_all(string=re.compile(e))
    
        # comment = return_comment(comment,f)
        # if comment=='':
        #     continue
        # comment = replace_kamek(comment,e,i)

    #######################################3   wla 7gaa
        # comment = soup.find_all(string=re.compile(e),limit=1)
        # f = new.find_all(string=re.compile(e))

        # comment = return_comment(comment,f)
        # if comment=='':
        #     continue
        # comment = replace_kamek(comment,e,i)
    ################################################   btrgm ICTT
        comment = soup.find(string=e)
        f = new.find_all(string=e)
    
        comment = return_comment(comment,f)
        if comment=='':
            continue
        comment = replace_kamek(comment,e,i)
    #################################################
        # comment = soup.find(string=re.compile(e))
        # f = new.find_all(string=e)
    
        # comment = return_comment(comment,f)
        # if comment=='':
        #     continue
        # comment = replace_kamek(comment,e,i)

    replace_and_create_file(html_directory)

    with codecs.open(html_directory, 'r', 'utf-8') as f:

        html = f.read()
    new = BeautifulSoup(html, 'html.parser')
    soup = BeautifulSoup(html, 'html.parser')
    # comments=[]
    for script in new(["script", "style"]):                   
        script.decompose() 
    for e,i in zip(origin,translated):
    
    ###############################################
        try:
            comment = soup.find(string=re.compile(e))
        except:
            continue
        f = new.find_all(string=re.compile(e))
    
        comment = return_comment(comment,f)
        if comment=='':
            continue
        comment = replace_kamek2(comment,e,i)
    replace_and_create_file(html_directory)









#to get the current working directory
# directory = os.getcwd()
# print(directory)

# # dir_path = os.path.join(directory,'**\*.html')
# dir_path = '**\*.html'
# print(dir_path)
# i=1
# print(glob.glob(dir_path, recursive=True))
# count = len(glob.glob(dir_path, recursive=True))
# for file in glob.glob(dir_path, recursive=True):
#     print("Html {} of {}".format(i,count))
#     print(file)
#     translate_html(file)
#     print("Done")
#     i+=1
# print("finished")

# import os

# # list to store txt files
# res = []
translate_html('E:/Coding Allstars/classcentral.github.io/university/umich.html')
# E:/Coding Allstars/classcentral.github.io/institution/amazon.html
# os.walk() returns subdirectories, file from current directory and 
# And follow next directory from subdirectory list recursively until last directory
# for root, dirs, files in os.walk(directory):
#     for file in files:
#         if file.endswith(".html"):
#             res.append(os.path.join(root, file))
# print(res)
# print(len(res))