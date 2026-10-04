import sys

def error_msg(msg):
    print(msg)
    sys.exit()

def is_bin(inp):

    inp_split = inp.split(".")


    lengths = [len(item) for item in inp_split]
    result = all(octet == 8 for octet in lengths)

    if result :
        for octect in inp_split:
            for char in octect:
                if char not in "01":
                    error_msg("invalid bin must contain digists of 0 or 1")
        return True
    else :
        try :
            for octect in inp_split:
                if not 0 <= int(octect) <= 255 :
                    error_msg("out of range")
            return False
        except ValueError:
            error_msg("invalid ipv4 ")
    
def ip_bin(inp):

    if is_bin(inp):

        result = []

        try :
            for octet in inp.split("."):
                if len(octet) == 8:
                    result.append(str(int(octet, 2)))
                else :
                    error_msg("invald bin must contain 8 digits")
            return ".".join(result)
        except ValueError:
            error_msg("invald bin must contain 8 digits")
    else :
        result = []
        
        try :
            for octet in inp.split("."):
                result.append(str(bin(int(octet))[2:]).zfill(8))
                
            return ".".join(result)
        except ValueError:
            error_msg("invald ipv4")

    
    

if __name__ == "__main__":

    inp = input(" => : ")
    print(ip_bin(inp))
                
