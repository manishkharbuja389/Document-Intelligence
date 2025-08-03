import re, tldextract, phonenumbers

def extract_indicators(text):
    indicators = {
        "domains": re.findall(r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}\b", text),
        "urls": re.findall(r"https?://[\w\-\.\?\=\&/]+", text),
        "ips": re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", text),
        "emails": re.findall(r"[\w\.-]+@[\w\.-]+", text),
        "phones": [match.raw_string for match in phonenumbers.PhoneNumberMatcher(text, None)],
        "socials": re.findall(r"(?:facebook|twitter|linkedin|t\.me|instagram|youtube)\.com/\S+", text),
        "tracking_ids": re.findall(r"UA-\d+-\d+|pub-\d+", text)
    }
    return indicators