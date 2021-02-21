def printer_error(s):
    #length of the string
    s_lenght=len(s)
    error_length = 0

    for x in s:
        #sort the string by looking for anything passed M
        if x not in "abcdefghijklm":
            #count errors
            error_length = error_length + 1
        else: 
            pass
    #create a variable to return it, so we can print it outside of the function
    msg = '{}/{}'.format(error_length,s_lenght)
    return msg
    #OR just
    #return error_length + "/" + s_lenght
