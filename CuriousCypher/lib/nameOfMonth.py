# lib/NameOfMonth.py

class MonthNames:
    def __init__(self):
        self.months = {
            "en": [
                "january", "february", "march", "april", "may", "june",
                "july", "august", "september", "october", "november", "december"
            ],
            "es": [
                "enero", "febrero", "marzo", "abril", 
                "mayo", "junio", "julio", "agosto", 
                "septiembre", "octubre", "noviembre", "diciembre"
            ],
            "id": [
                "januari", "februari", "maret", "april", 
                "mei", "juni", "juli", "agustus", 
                "september", "oktober", "november", "desember"
            ],
            "hi": [
                "जनवरी", "फरवरी", "मार्च", "अप्रैल", 
                "मई", "जून", "जुलाई", "अगस्त", 
                "सितंबर", "अक्टूबर", "नवंबर", "दिसंबर"
            ],
            "th": [
                "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", 
                "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", 
                "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"
            ],
            "ph": [
                "enero", "pebrero", "marso", "abril", 
                "mayo", "hunyo", "hulyo", "agosto", 
                "setyembre", "oktubre", "nobyembre", "disyembre"
            ],
            "vn": [
                "tháng một", "tháng hai", "tháng ba", "tháng tư", 
                "tháng năm", "tháng sáu", "tháng bảy", "tháng tám", 
                "tháng chín", "tháng mười", "tháng mười một", "tháng mười hai"
            ]
        }

    def get_months(self, lang_code):
        """Return the list of months in the specified language code."""
        return self.months.get(lang_code, [])

