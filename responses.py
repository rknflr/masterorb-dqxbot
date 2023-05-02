
import orb

def handle_response(message) -> str:
    p_message = message

    """if p_message == 'hello':
        return 'Hey There!'

    if p_message == 'roll':
        return str(random.randint(1,6))

    if p_message == '!help':
        return "`This is a help message`" """
    
    if p_message.startswith("!jewel"):
        return (orb.orb_result(p_message[7:]))
        #return orb.orb_result(p_message[7:])