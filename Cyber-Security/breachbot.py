#Breach Bot Starter Code
breachyear = 2017

#Greets user
print("Hello! I'm Breachbot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachyear
print("Wow! That means it has been " + str(timePassed) + " years since the National Health Services data breach!")


#Introduces Breach
print("Would you like to learn about the 2017 National Health Services data breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("In 2017, UK Hospitals were hit with a ransomware attack that resulted in 16 hospitals being shut down. National Health Service files were put at risk. ")
    print("The attack froze all systems and encyrpted files. Any computers that were attempted to be accessed from employees displayed a demand for $300 in bitcoin as a form of ransomware. ")
    print("The Wanna Decryptor (Wanna Cry) ransomware strain attacked the data at several hospitals. Similar attacks infected computers across the European continent, exploiting EternalBlue (developed by the NSA) to break through Windows security. ")
    
  elif topic.lower() == "b":
    print("Luckily, no patient data seemed to be compromised during the breach. However, it greatly affected the hospitals that were put under attack. General chaos led to many appointments requiring cancelation and made it hard to access simple medical records. Operations have been postponed and a lot of money has been put into recovering from the ransomware attack. No users were directly affected because the data is believed to not have been breached, just threatened. Although controversial, FBI reccomendation was that the hospital pay to get their files decrypted following the attack, which would aide in lessening chaos and complications that patients faced. ")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Introduces My Take
print("\n I'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relate to the CIA Triad, (b) my reaction, (c) my advice, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("The confidentiality of users healthcare information was at risk when information that was meant to be private was able to be accessed by the facilitators of the breach.")
    
  elif topic.lower() == "b":
    print("We agree with the organization's response because they did their best to limit chaos, acknowledging the fact that while information was put at risk, it was not actually leaked. The main goal was to maintain a sense of calm, and working on going back to a normal system with extra precaution was the best step they could take. ")

  elif topic.lower() == "c":
    print("I would convince victims to take action by making sure they are mindful of the information they are sharing, because they never know where it might end up. My advice would be to keep their passwords and private information very secure and hard to guess or hack easily. They should make sure websites and apps they use do not take their data to publish or sell, which could also put them at risk. ")
  
  elif topic.lower() == "d":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")
