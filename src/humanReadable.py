import re
def format_duration(seconds):
    str_ = ''
    years = seconds // 31536000
    days = (seconds - years * 31536000) // 86400
    hour = ((seconds - years * 31536000) - days * 86400) // 3600
    min_ = (((seconds - years * 31536000) - days * 86400) - hour * 3600) // 60
    sec = (((seconds - years * 31536000) - days * 86400) - hour * 3600) - min_ * 60
    
    year_ = ''
    days_=''
    hour_=''
    min__=''
    sec_=''
    if years == 0: year_
    if days == 0: days_
    if hour == 0: hour_
    if min_ == 0: min__
    if sec == 0: sec_
    
    if years == 1: year_ = str(years) + ' year'
    if days == 1: days_ = str(days) + ' day'
    if hour == 1: hour_ = str(hour) + ' hour'
    if min_ == 1: min__ = str(min_) + ' minute'
    if sec == 1: sec_ = str(sec) + ' second'
    
    if years > 1: year_ = str(years) + ' years'
    if days > 1: days_ = str(days) + ' days'
    if hour > 1: hour_ = str(hour) + ' hours'
    if min_ > 1: min__ = str(min_) + ' minutes'
    if sec > 1: sec_ = str(sec )+ ' seconds'
    
    str_ = f'{year_}, {days_}, {hour_}, {min__}, {sec_}'
    
    res = re.findall(r'\d+\s\w+', str_)
    
    if seconds == 0:
        return 'now'
    elif len(res) == 1:
        return ' '.join(res)
    else:
        res[-1] = f'and {res[-1]}'
        for i in range(len(res) - 2):
            res[i] = f'{res[i]},'
        return ' '.join(res)
        
print(format_duration(8))
