#!/usr/bin/env python3
import random
import os

os.system('clear')

print('''
      ___           ___           ___       ___ 
     /\  \         /\  \         /\__\     /\__\,
    /::\  \       /::\  \       /:/  /    /:/  /
   /:/\:\  \     /:/\:\  \     /:/  /    /:/  / 
  /::\~\:\  \   /:/  \:\  \   /:/  /    /:/  /  
 /:/\:\ \:\__\ /:/__/ \:\__\ /:/__/    /:/__/   
 \/_|::\/:/  / \:\  \ /:/  / \:\  \    \:\  \   
    |:|::/  /   \:\  /:/  /   \:\  \    \:\  \  
    |:|\/__/     \:\/:/  /     \:\  \    \:\  \ 
    |:|  |        \::/  /       \:\__\    \:\__\,
     \|__|         \/__/         \/__/     \/__/

      ___           ___           ___     
     /\  \         /\__\         /\  \    
     \:\  \       /:/  /        /::\  \   
      \:\  \     /:/__/        /:/\:\  \  
      /::\  \   /::\  \ ___   /::\~\:\  \ 
     /:/\:\__\ /:/\:\  /\__\ /:/\:\ \:\__\,
    /:/  \/__/ \/__\:\/:/  / \:\~\:\ \/__/
   /:/  /           \::/  /   \:\ \:\__\  
   \/__/            /:/  /     \:\ \/__/  
                   /:/  /       \:\__\    
                   \/__/         \/__/    

      ___                       ___           ___     
     /\  \          ___        /\  \         /\  \    
    /::\  \        /\  \      /::\  \       /::\  \   
   /:/\:\  \       \:\  \    /:/\:\  \     /:/\:\  \  
  /:/  \:\__\      /::\__\  /:/  \:\  \   /::\~\:\  \ 
 /:/__/ \:|__|  __/:/\/__/ /:/__/ \:\__\ /:/\:\ \:\__\,
 \:\  \ /:/  / /\/:/  /    \:\  \  \/__/ \:\~\:\ \/__/
  \:\  /:/  /  \::/__/      \:\  \        \:\ \:\__\  
   \:\/:/  /    \:\__\       \:\  \        \:\ \/__/  
    \::/__/      \/__/        \:\__\        \:\__\    
     ~~                        \/__/         \/__/    

Use these virtual dice when you leave your real dice at home.
''')

def rolling():
    input("Press <Enter> to role the dice. <Ctrl-c> to quit.")

    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)

    if d1 == 1:
        print('''
    ╔═══════╗
    ║       ║
    ║   *   ║
    ║       ║
    ╚═══════╝''')


    if d1 == 2:
        print("""
    ╔═══════╗
    ║     * ║
    ║       ║
    ║ *     ║
    ╚═══════╝""")


    if d1 == 3:
        print("""
    ╔═══════╗
    ║ *     ║
    ║   *   ║
    ║     * ║
    ╚═══════╝""")


    if d1 == 4:
        print("""
    ╔═══════╗
    ║ *   * ║
    ║       ║
    ║ *   * ║
    ╚═══════╝""")


    if d1 == 5:
        print("""
    ╔═══════╗
    ║ *   * ║
    ║   *   ║
    ║ *   * ║
    ╚═══════╝""")


    if d1 == 6:
        print("""
    ╔═══════╗
    ║ *   * ║
    ║ *   * ║
    ║ *   * ║
    ╚═══════╝""")

    if d2 == 1:
        print('''
    ╔═══════╗
    ║       ║
    ║   *   ║
    ║       ║
    ╚═══════╝''')


    if d2 == 2:
        print("""
    ╔═══════╗
    ║     * ║
    ║       ║
    ║ *     ║
    ╚═══════╝""")


    if d2 == 3:
        print("""
    ╔═══════╗
    ║ *     ║
    ║   *   ║
    ║     * ║
    ╚═══════╝""")


    if d2 == 4:
        print("""
    ╔═══════╗
    ║ *   * ║
    ║       ║
    ║ *   * ║
    ╚═══════╝""")


    if d2 == 5:
        print("""
    ╔═══════╗
    ║ *   * ║
    ║   *   ║
    ║ *   * ║
    ╚═══════╝""")


    if d2 == 6:
        print("""
    ╔═══════╗
    ║ *   * ║
    ║ *   * ║
    ║ *   * ║
    ╚═══════╝""")

    if d1 == d2 and d1 != 1:
        print("WHAT LUCK YOU HAVE!")

    if d1 == 1 and d2 == 1:
        print("SNAKE EYES!! YOU LOSE!")

    print(" ")

rolling()
