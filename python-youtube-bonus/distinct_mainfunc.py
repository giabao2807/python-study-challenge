#*************************************
# if __name__ == '__main__'
#*************************************

#1. Module can be run as a stadalone program
#2. Module can be imported and used by other modules

#Python interprester sets "special variables", one of which is __name__
#then python wil execute the code found within __main__

def main():
    print("Hello")


if __name__=='__main__':
    main()