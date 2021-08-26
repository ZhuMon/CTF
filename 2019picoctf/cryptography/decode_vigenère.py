
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():

    table = []
    with open("./table.txt", 'r') as f:
        lines = f.readlines()
        # load table
        for line in lines[2:28]:
            row = []
            for col in line[4:56:2]:
                row.append(col)
            table.append(row)

        # load cipher
        cipher = "UFJKXQZQUNB"
        
        # load key
        key = "SOLVECRYPTO"
        # decode
        plaintext = ""
        for k, c in zip(key, cipher.replace(' ', '').replace('{','').replace('}','')):
            k_index = ALPHABET.index(k)
            c_index = ALPHABET.index(c)

            plaintext += table[c_index][k_index]

        # add blank
        for c, i in zip(cipher, range(0,len(cipher))):
            replace_char = ' ' if c == ' ' else '{' if c == '{' else '}' if c == '}' else ''
            plaintext = plaintext[:i] + replace_char + plaintext[i:]
            
    

        print(plaintext)
        

if __name__ == "__main__":
    main()
