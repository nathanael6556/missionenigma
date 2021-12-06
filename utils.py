def number_of_word(text):
    return text.strip().count(' ') + 1

def td_to_srt_time(time):
    srt_time = str(time)

    if('.' in srt_time):
        # srt time uses ',' instead of '.'
        srt_time = srt_time.replace('.', ',')

        # Remove the trailing zeroes
        srt_time = srt_time[:-3]
    else:
        srt_time += ",000"
    
    # Add a zero in front if the hour is single digit
    if(srt_time.startswith('0:')):
        srt_time = '0' + srt_time
    
    return srt_time
    