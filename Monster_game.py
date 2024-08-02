#TextBasedGame.py
#Alegria S. Forman
#IT-140 | Dr. Michael Moran

#Defined main function for the game.
def main():
    #Display background and instructions for moving between room and how to collect weapons
    print('*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>\n')
    print('| Pizac has taken over the village. Gather all weapons to defeat Pizac |')
    print('|Get the MAP LIST first from the Office to find the rest of the weapons| ')
    print('|  To get weapons, enter the weapon name to be added to the inventory  |')
    print('\n|   Move To Each Rooms By Entering: North, South, East, West or Exit   |')
    print('\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>')
    # This is the dictionary linking from room to other rooms.
    ubok = {
        'Receiving Hall': {'NORTH': 'Bed Chamber', 'SOUTH': 'Chapel', 'EAST': 'Kitchen', 'WEST': 'Office'},
        'Bed Chamber': {'SOUTH': 'Receiving Hall', 'EAST': 'Garderobe', 'weapon': 'FEATHER'},
        'Garderobe': {'WEST': 'Bed Chamber', 'weapon': 'SWORD'},
        'Chapel': {'EAST': 'Cellar', 'NORTH': 'Receiving Hall', 'weapon': 'ARMOR'},
        'Cellar': {'WEST': 'Chapel', 'weapon': 'SHIELD'},
        'Office': {'EAST': 'Receiving Hall', 'weapon': 'MAP LIST'},
        'Kitchen': {'NORTH': 'Great Hall', 'WEST': 'Receiving Hall', 'weapon': 'BOW & ARROWS'},
        'Great Hall': {'SOUTH': 'Kitchen'}
    }

    current_ubok = 'Receiving Hall'#Start where player is located
    weapon_inventory = []#Variable where weapons will be stored when player collects them
    #Definition function for player status on where player is currently located, inventory of weapons and DRY method of coding
    def status():
        print('---  S T A T U S ---')
        print('You are currently located in ', current_ubok, '.')
        print('Weapon available:', weapon_inventory)
        print('\n-*-*-*-*-*-*-*-*-*-*-*-*\n')

    #Definition function to get data entry from player to collect weapons
    def get_weapon(current_ubok):
        collect_weapon = input('What would you like to do. Collect: ').upper()#Data input from player and all upper case
        if collect_weapon == ubok[current_ubok]['weapon']:#If data input is equal to weapon in dictionary, then will append to weapon_inventory list
            weapon_inventory.append(ubok[current_ubok]['weapon'])
            status()#status function calling to show where player is currently located and weapon inventory list
        elif collect_weapon != ubok[current_ubok]['weapon']:#If data input is not equal to weapon in dictionary, then will prompt players to collect and re-enter
            print('\nCheck your entry. Try again.')
            collect_weapon = input('What would you like to do. Collect: ').upper()
            weapon_inventory.append(ubok[current_ubok]['weapon'])
        else:#If data input is not equal to weapon in dictionary for the second time, then will prompt players to collect and re-enter again
            print('\nPlease try again.')
            collect_weapon = input('What would you like to do. Collect: ').upper()
            weapon_inventory.append(ubok[current_ubok]['weapon'])

    while True:#Start loop on game and different messages to player when certain conditions are met.
        if current_ubok == 'Receiving Hall':#Players start in Receving Hall and prompts to get the Map List from Office first, otherwise, player won't know where weapons are
            if len(weapon_inventory) == 0:
                print(
                    '\nYou are currently in the Receiving Hall. Go to the Office where you can find the Map List. Without it you will be lost and will not find the other weapons to defeat Pizac. WALK WEST.')
                print('\n-*-*-*-*-*-*-*-*-*-*-*-*\n')
                status()#status function calling to show where player is currently located and weapon inventory list

            if len(weapon_inventory) == 1 and len(weapon_inventory) == 3:#Additional message to player when there are 1 and 3 weapons in inventory
                print(
                    'You are currently in the Receiving Hall again. Be very quiet, to get more weapons... enter NORTH or SOUTH.')
                status()#status function calling to show where player is currently located and weapon inventory list

            if len(weapon_inventory) == 5:#Additional message to player when there are 5 weapons in inventory
                print(
                    'You are currently in the Receiving Hall. The last weapon is hidden in the Kitchen. Victory is at hand to defeat Pizac. WALK EAST')
                status()#status function calling to show where player is currently located and weapon inventory list

            if len(weapon_inventory) == 6:#Additional message to player when there are 6 weapons in inventory
                print(
                    'The entire village flooded the Receiving Hall! They picked you up in their shoulders and shouted - Horrah to our hero! Udat Palu is so grateful, he made you his right hand and successor!!!')
                print('\n-*-*-*-*-*-*-*-*-*-*-*-*\n')
                exit(0)
        if current_ubok == 'Bed Chamber':#Message to player if weapon inventory list are met depending if they went north or south after visiting the Office to avoid dup messages
            if len(weapon_inventory) == 1 or weapon_inventory == ['MAP LIST', 'ARMOR', 'SHIELD']:#Message to player when there are 1 and ['MAP LIST', 'ARMOR', 'SHIELD'] weapons in inventory
                print(
                    'You are currently in the Bed Chamber. You see a big Feather sticking out from a pillow. If all weapons fail, you can use the Feather to tikle Pizac to death. In the Garderobe, another weapon is hidden. COLLECT FEATHER, then WALK EAST')
                weapon = get_weapon(current_ubok)
                weapon_inventory.append(weapon)
                weapon_inventory = list(filter(None, weapon_inventory))#Code where "None" from list will be removed every time weapon is appended
                status()#status function calling to show where player is currently located and weapon inventory list

            if len(weapon_inventory) >= 5 or weapon_inventory == ['MAP LIST', 'FEATHER', 'SWORD']:#Message to player when there are equal to or greater than 5 and ['MAP LIST', 'FEATHER', 'SWORD'] weapons in inventory
                print(
                    '\nYou are currently in the Bed Chamber again. Check your Map list if you missed any weapons in other rooms.')
                status()#status function calling to show where player is currently located and weapon inventory list

        if current_ubok == 'Garderobe':#Message to player if weapon inventory list are met depending if they went north or south after visiting the Office
            if weapon_inventory == ['MAP LIST', 'FEATHER'] or len(weapon_inventory) == 4:#Message to player when there are 4 and ['MAP LIST', 'FEATHER'] weapons in inventory
                print(
                    'You are currently in the Garderobe. In the corner you saw a shiny Sword behind some robes. Hurry and take it. Go back to the Bed Chamber. COLLECT SWORD, then WALK WEST. ')
                weapon = get_weapon(current_ubok)
                weapon_inventory.append(weapon)
                weapon_inventory = list(filter(None, weapon_inventory))
                status()#status function calling to show where player is currently located and weapon inventory list

            if len(weapon_inventory) == 5:#Error message to player that weapon was already collected, and when there are 5 weapons in inventory
                print('You collected the weapon already, walk WEST.')
                status()#status function calling to show where player is currently located and weapon inventory list

        if current_ubok == 'Chapel':#Message to player if weapon inventory list are met depending if they went north or south after visiting the Office
            if len(weapon_inventory) == 1 or weapon_inventory == ['MAP LIST', 'FEATHER', 'SWORD']:#Message to player when there are 1 and ['MAP LIST', 'FEATHER', 'SWORD'] weapons in inventory
                print(
                    'You are currently in the Chapel. At the altar, you spotted the Armor hidden behind the curtains. Wear it quickly! Another weapon awaits in the Cellar. WEAR ARMOR, then WALK EAST.')
                weapon = get_weapon(current_ubok)
                weapon_inventory.append(weapon)
                weapon_inventory = list(filter(None, weapon_inventory))#Code where "None" from list will be removed every time weapon is appended
                status()#status function calling to show where player is currently located and weapon inventory list

            else:
                if len(weapon_inventory) >= 4:#Error message to player that weapon was already collected and equal or more than 4 weapons in inventory
                    print('You are currently in the Chapel again. Go Back to the Receiving Hall. WALK NORTH')
                    status()#status function calling to show where player is currently located and weapon inventory list

        if current_ubok == 'Cellar':#Message to player if weapon inventory list are met depending if they went north or south after visiting the Office
            if len(weapon_inventory) == 2 or weapon_inventory == ['MAP LIST', 'FEATHER', 'SWORD', 'ARMOR']:#Message to player when there are 2 and ['MAP LIST', 'FEATHER', 'SWORD', 'ARMOR'] weapons in inventory
                print(
                    'You are currently in the Cellar. You see a Shield hung on the wall behind some wine barrels. You are close to defeating Pizac, go back to the Chapel. COLLECT SHIELD, then WALK WEST ')
                weapon = get_weapon(current_ubok)
                weapon_inventory.append(weapon)
                weapon_inventory = list(filter(None, weapon_inventory))#Code where "None" from list will be removed every time weapon is appended
                status()#status function calling to show where player is currently located and weapon inventory list
            else:#Error message to player if weapon inventory list are not met
                print('You collected the weapon already.')

        if current_ubok == 'Office':
            if len(weapon_inventory) == 0:#Message to player where the Map list is located
                print(
                    'You are currently in the Office. You glimpsed a Map list under a gas lamp. Go back to the Receiving Hall. COLLECT MAP LIST, then WALK EAST.')
                weapon = get_weapon(current_ubok)
                weapon_inventory.append(weapon)
                weapon_inventory = list(filter(None, weapon_inventory))#Code where "None" from list will be removed every time weapon is appended
                status()#status function calling to show where player is currently located and weapon inventory list

            else:#Message to player when the Map list is already collected
                print('You collected the map list already. Go back to the Receiving Hall. WALK EAST.')

        if current_ubok == 'Kitchen':
            if len(weapon_inventory) <= 4:#The message to player if it has less than or equal to 4, warning to get the other weapons first or player losses
                print(
                    'You are entering the Kitchen. You are too close to the Great Hall where Pizac is nearby. You will sustain life threatening injuries. Collect the rest of the weapons or exit. WALK WEST.')
                status()#status function calling to show where player is currently located and weapon inventory list

            if len(weapon_inventory) == 5:#The message if player has all weapons except for what is hidden on the kitchen
                print(
                    'You are currently in the Kitchen. By the fireplace, you see behind the cabinet pantry the bow and arrows. This is the last weapon. You are ready to fight Pizac. COLLECT BOW & ARROWS, then WALK NORTH.')
                weapon = get_weapon(current_ubok)
                weapon_inventory.append(weapon)
                weapon_inventory = list(filter(None, weapon_inventory))
                status()#status function calling to show where player is currently located and weapon inventory list

            else:
                if len(weapon_inventory) == 6:#The message if player has all weapons to head to Receiving Hall where all villagers await and will celebrate
                    print(
                        'You are in the Kitchen and vanquished Pizac the terror. The entire village awaits to celebrate your bravery and success in the Receiving hall! WALK WEST.')
                    print('\n-*-*-*-*-*-*-*-*-*-*-*-*\n')

        if current_ubok == 'Great Hall':#When player is in the Great Hall where Pizac is located, different set of display depending on weapon inventory.
            if len(weapon_inventory) <= 5:#If player has equal to and lesser than 5 weapons, player will die.
                print('You are currently in the Great Hall. You look up... Pizac the terror is awake.')
                print('You do not have enough weapon to defend yourself... Pizac swatted you with his sharp claws...')
                print('\nSorry you lost!')
                exit(0)
            if len(weapon_inventory) == 6:#If player has 6 weapons, player will win.
                print('You are currently in the Great Hall. You look up... Pizac the terror is awake.')
                print('You rush towards Pizac using your Sword.')
                print('\n-*-*-*-*-*-*-*-*-*-*-*-*\n')
                print(
                    'Pizac swung his tail and try to  stun you. You jumped high and did a somesault. You managed to hit his shoulders, stomach and legs. He is certain he will be defeated and tries to flee...')
                print('\n-*-*-*-*-*-*-*-*-*-*-*-*\n')
                print(
                    'You have the advantage and want to end this once and for all. You use your bow and arrow... Alas! It pierced his heart. Pizac is suffering so you used the feather out of mercy... He is at peace, VICTORY!')
                print('\nGo to the Kitchen. WALK SOUTH')
                print('\n-*-*-*-*-*-*-*-*-*-*-*-*\n')

        command_direx = input('Enter North; South; East; West; or Exit: ').upper()#Data input from player what direction to go or exit

        if command_direx == 'EXIT':#If data input entered is exit, the game stops
            current_ubok = 'EXIT'
            print('Goodbye.')
            print('\n-*-*-*-*-*-*-*-*-*-*-*-*')
            break

        if command_direx in ubok[current_ubok]:#Prompt to indicate where the player is currently located and weapon inventory
            current_ubok = ubok[current_ubok][command_direx]
            status()#status function calling to show where player is currently located and weapon inventory list

        else:
            print('\nYou cannot go that direction')#Prompt to indicate where the player entered direction incorrectly and to try again
            status()#status function calling to show where player is currently located and weapon inventory list

main()#Call main function

