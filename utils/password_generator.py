import secrets
import string
import re
import math
from .password_rules import PLATFORM_RULES, validate_password_for_platform

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.numbers = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.similar_chars = "il1Lo0O"
    
    def generate_platform_password(self, platform, length=None, difficulty='medium'):
        """Generate password based on platform rules"""
        rules = PLATFORM_RULES.get(platform.lower())
        if not rules:
            raise ValueError(f"Platform '{platform}' not supported")
        
        # Use platform's recommended length or user specified
        if length is None:
            length = max(rules['min_length'], 12)
        else:
            length = max(min(length, rules['max_length']), rules['min_length'])
        
        # Build character set based on rules
        charset = ""
        guaranteed_chars = []
        
        if rules['require_lowercase'] or not any([rules['require_uppercase'], rules['require_numbers'], rules['require_symbols']]):
            charset += self.lowercase
            guaranteed_chars.append(secrets.choice(self.lowercase))
        
        if rules['require_uppercase']:
            charset += self.uppercase
            guaranteed_chars.append(secrets.choice(self.uppercase))
        
        if rules['require_numbers']:
            charset += self.numbers
            guaranteed_chars.append(secrets.choice(self.numbers))
        
        if rules['require_symbols']:
            charset += self.symbols
            guaranteed_chars.append(secrets.choice(self.symbols))
        
        # Remove forbidden characters
        for forbidden in rules['forbidden_chars']:
            charset = charset.replace(forbidden, '')
        
        # Apply difficulty settings
        if difficulty == 'easy':
            charset = charset.replace(self.similar_chars, '')
        elif difficulty == 'hardest':
            charset += "~`!@#$%^&*()_-+={}[]|\\:;\"'<>,.?/"
        
        # Generate remaining characters
        remaining_length = length - len(guaranteed_chars)
        additional_chars = [secrets.choice(charset) for _ in range(remaining_length)]
        
        # Combine and shuffle
        all_chars = guaranteed_chars + additional_chars
        password = ''.join(secrets.choice(all_chars) for _ in range(len(all_chars)))
        
        # Shuffle the password
        password_list = list(password)
        for i in range(len(password_list)):
            j = secrets.randbelow(len(password_list))
            password_list[i], password_list[j] = password_list[j], password_list[i]
        
        password = ''.join(password_list)
        
        # Calculate strength and entropy
        strength = self.calculate_strength(password)
        entropy = self.calculate_entropy(password, charset)
        
        return {
            'password': password,
            'strength': strength,
            'entropy': entropy,
            'rules': self._get_applied_rules(rules, length)
        }
    
    def generate_custom_password(self, length, uppercase=True, lowercase=True, 
                                numbers=True, symbols=True, difficulty='medium'):
        """Generate password with custom rules"""
        charset = ""
        guaranteed_chars = []
        
        if lowercase:
            charset += self.lowercase
            guaranteed_chars.append(secrets.choice(self.lowercase))
        
        if uppercase:
            charset += self.uppercase
            guaranteed_chars.append(secrets.choice(self.uppercase))
        
        if numbers:
            charset += self.numbers
            guaranteed_chars.append(secrets.choice(self.numbers))
        
        if symbols:
            charset += self.symbols
            guaranteed_chars.append(secrets.choice(self.symbols))
        
        if not charset:
            raise ValueError("At least one character type must be selected")
        
        # Apply difficulty settings
        if difficulty == 'easy':
            charset = ''.join(c for c in charset if c not in self.similar_chars)
        elif difficulty == 'hardest':
            charset += "~`!@#$%^&*()_-+={}[]|\\:;\"'<>,.?/"
        
        # Generate remaining characters
        remaining_length = max(0, length - len(guaranteed_chars))
        additional_chars = [secrets.choice(charset) for _ in range(remaining_length)]
        
        # Combine and shuffle
        all_chars = guaranteed_chars[:length] + additional_chars
        password_list = list(''.join(all_chars)[:length])
        
        # Shuffle the password
        for i in range(len(password_list)):
            j = secrets.randbelow(len(password_list))
            password_list[i], password_list[j] = password_list[j], password_list[i]
        
        password = ''.join(password_list)
        
        # Calculate strength and entropy
        strength = self.calculate_strength(password)
        entropy = self.calculate_entropy(password, charset)
        
        return {
            'password': password,
            'strength': strength,
            'entropy': entropy,
            'rules': self._get_custom_rules(length, uppercase, lowercase, numbers, symbols)
        }
    
    def calculate_strength(self, password):
        """Calculate password strength with detailed feedback"""
        score = 0
        feedback = []
        
        # Length scoring
        length = len(password)
        if length >= 12:
            score += 25
        elif length >= 8:
            score += 15
        elif length >= 6:
            score += 10
        else:
            feedback.append("Use at least 8 characters")
        
        # Character variety scoring
        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_symbol = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password))
        
        char_variety = sum([has_lower, has_upper, has_digit, has_symbol])
        score += char_variety * 15
        
        if not has_lower:
            feedback.append("Add lowercase letters")
        if not has_upper:
            feedback.append("Add uppercase letters")
        if not has_digit:
            feedback.append("Add numbers")
        if not has_symbol:
            feedback.append("Add special characters")
        
        # Pattern detection (reduce score for common patterns)
        if re.search(r'(.)\1{2,}', password):  # Repeated characters
            score -= 10
            feedback.append("Avoid repeated characters")
        
        if re.search(r'(012|123|234|345|456|567|678|789|890)', password):
            score -= 15
            feedback.append("Avoid sequential numbers")
        
        if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password.lower()):
            score -= 15
            feedback.append("Avoid sequential letters")
        
        # Common password patterns
        common_patterns = ['password', '123456', 'qwerty', 'admin', 'login']
        for pattern in common_patterns:
            if pattern in password.lower():
                score -= 20
                feedback.append("Avoid common words")
                break
        
        # Ensure score is within bounds
        score = max(0, min(100, score))
        
        # Determine strength level
        if score >= 80:
            level = "Very Strong"
            color = "#00aa00"
        elif score >= 60:
            level = "Strong"
            color = "#66aa00"
        elif score >= 40:
            level = "Medium"
            color = "#ffaa00"
        elif score >= 20:
            level = "Weak"
            color = "#ff6600"
        else:
            level = "Very Weak"
            color = "#ff0000"
        
        return {
            'score': score,
            'level': level,
            'color': color,
            'feedback': feedback
        }
    
    def calculate_entropy(self, password, charset):
        """Calculate password entropy"""
        if not password or not charset:
            return 0
        
        charset_size = len(set(charset))
        entropy = len(password) * math.log2(charset_size)
        return round(entropy, 2)
    
    def _get_applied_rules(self, rules, length):
        """Get human-readable rules that were applied"""
        applied = [f"{length} characters"]
        
        if rules['require_uppercase']:
            applied.append("Uppercase letters")
        if rules['require_lowercase']:
            applied.append("Lowercase letters")
        if rules['require_numbers']:
            applied.append("Numbers")
        if rules['require_symbols']:
            applied.append("Special characters")
        
        return applied
    
    def _get_custom_rules(self, length, uppercase, lowercase, numbers, symbols):
        """Get human-readable custom rules"""
        applied = [f"{length} characters"]
        
        if uppercase:
            applied.append("Uppercase letters")
        if lowercase:
            applied.append("Lowercase letters")
        if numbers:
            applied.append("Numbers")
        if symbols:
            applied.append("Special characters")
        
        return applied
