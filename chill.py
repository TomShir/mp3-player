#Importing the necessary modules 
import time 
import sys 
from colorama import Fore 
import os 
from playsound import playsound 
import pyttsx3 
pyttsx3.init()
colors=[Fore.GREEN,Fore.CYAN,Fore.BLUE,Fore.RED,Fore.RESET]
current_mp3_files=['blaze.mp3','Fighter.mp3','survivor_instrumental.mp3','Survivor.mp3','TRACER.mp3','reboot.mp3','setsuna.mp3',]
def loop_over(sequence,color,delay_time):
    for text in sequence:
        sys.stdout.flush()
        time.sleep(delay_time)
        sys.stdout.write(f'{color}{text}')
    else:
        print(f'{colors[-1]}')
        
open_text_file=open('mymp3.txt','r')
read_all_lines=open_text_file.readlines()
count=0
loop_over(sequence=f'mp3 files:\n\t',color=colors[0],delay_time=0.1)
for line in read_all_lines:
    time.sleep(0.1)
    count+=1 
    print(f'\v{colors[1]}{count}. {line}',flush=True)
else:
    print(f'{colors[-1]}')
    time.sleep(1)
    input_name_of_mp3_file=input('Enter the name of the mp3 file you want to play:')
    while input_name_of_mp3_file[input_name_of_mp3_file.index('.')+1:]!='mp3' or input_name_of_mp3_file not in current_mp3_files:
        time.sleep(1)
        loop_over(sequence='Error,this Python program only plays mp3 files that are present in your collection of files, please try again',color=colors[-2],delay_time=0.1)
        time.sleep(0.1)
        input_name_of_mp3_file=input('Enter the name of the mp3 file you want to play:')
    else:
        try:
            time.sleep(1)
            how_many_times_mp3_file_must_be_played=int(input(f'How many times do you want to play {input_name_of_mp3_file}?:'))
            time.sleep(1)
            for n in range(how_many_times_mp3_file_must_be_played):
                current_number=n
                if current_number==0:
                    pyttsx3.speak(f'{input_name_of_mp3_file} playing for the first time')
                    time.sleep(1)
                    playsound(input_name_of_mp3_file)
                elif current_number==1:
                    pyttsx3.speak(f'{input_name_of_mp3_file} playing for the second time')
                    playsound(input_name_of_mp3_file)
                elif current_number==2:
                    pyttsx3.speak(f'{input_name_of_mp3_file} playing for the third time')
                    playsound(input_name_of_mp3_file)
                elif current_number==3:
                    pyttsx3.speak(f'{input_name_of_mp3_file} playing for the fourth time')
                    time.sleep(1)
                    playsound(input_name_of_mp3_file)
                elif current_number==4:
                     pyttsx3.speak(f'{input_name_of_mp3_file} playing for the fifth time')
                     time.sleep(1)
                     playsound(input_name_of_mp3_file)
                elif current_number==5:
                     pyttsx3.speak(f'{input_name_of_mp3_file} playing for the sixth time')
                     time.sleep(1)
                     playsound(input_name_of_mp3_file)
                elif current_number==6:
                     pyttsx3.speak(f'{input_name_of_mp3_file} playing for the seventh time')
                     playsound(input_name_of_mp3_file)
                elif current_number==7:
                    pyttsx3.speak(f'{input_name_of_mp3_file} playing for the eighth time')
                    playsound(input_name_of_mp3_file)
                elif current_number==8:
                     pyttsx3.speak(f'{input_name_of_mp3_file} playing for the ningth time')
                     playsound(input_name_of_mp3_file)
                elif current_number==9:
                      pyttsx3.speak(f'{input_name_of_mp3_file} playing for the tenth time')
                      playsound(input_name_of_mp3_file)
            else:
                if how_many_times_mp3_file_must_be_played!=1:
                 time.sleep(1)
                 pyttsx3.speak(f'{input_name_of_mp3_file} was played for the last time')
                 sys.exit('')
        except ValueError:
            loop_over(sequence='Error,you entered an invalid value',color=colors[0],delay_time=0.1)
