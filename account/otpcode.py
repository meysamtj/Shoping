import random


class OTPGenerator:
    def __init__(self, length=6):
        self.length = length

    def generate_otp(self):
        digits = "ABCDEFGHJKLMNOPQRSTUVWXYZ0123456789"
        otp = ""
        for i in range(self.length):
            otp += digits[random.randint(0, 34)]
            
        return otp


# otp_gen = OTPGenerator()
# otp = otp_gen.generate_otp()
# print("Generated OTP:", otp)
