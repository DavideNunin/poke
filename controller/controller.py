from  model.model.py import Model
import math
class Controller():
    def calculate_capture_rate(hp_max=0,hp_c=0,rate=0,bonus_ball=0,bonus_status=0):
        a = ((3*hp_max-2*hp_c)*rate*bonus_ball)/(3*hp_max)*bonus_status
        b = 1048560/(math.sqrt(math.sqrt(16711680/a)))
        final_value=(b/65535)**4
        return final_value
    def get_capture_rate(name,hp_max,hp_c,bonus_ball,bonus_status):
        rate= model.get_rate(name)
        return calculate_capture_rate(hp_max,hp_c,rate,bonus_ball,bonus_status)
