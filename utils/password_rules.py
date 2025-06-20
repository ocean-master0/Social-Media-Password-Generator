# """
# Platform-specific password rules and requirements
# """

# PLATFORM_RULES = {
#     'facebook': {
#         'name': 'Facebook',
#         'min_length': 6,
#         'max_length': 50,
#         'require_uppercase': True,
#         'require_lowercase': True,
#         'require_numbers': True,
#         'require_symbols': True,
#         'forbidden_chars': [],
#         'description': 'Facebook allows flexible passwords with minimum 6 characters'
#     },
#     'instagram': {
#         'name': 'Instagram',
#         'min_length': 6,
#         'max_length': 30,
#         'require_uppercase': False,
#         'require_lowercase': True,
#         'require_numbers': True,
#         'require_symbols': False,
#         'forbidden_chars': [],
#         'description': 'Instagram requires at least 6 characters with numbers recommended'
#     },
#     'whatsapp': {
#         'name': 'WhatsApp',
#         'min_length': 4,
#         'max_length': 64,
#         'require_uppercase': False,
#         'require_lowercase': True,
#         'require_numbers': False,
#         'require_symbols': False,
#         'forbidden_chars': [],
#         'description': 'WhatsApp has minimal requirements, 4+ characters'
#     },
#     'twitter': {
#         'name': 'Twitter/X',
#         'min_length': 8,
#         'max_length': 50,
#         'require_uppercase': True,
#         'require_lowercase': True,
#         'require_numbers': True,
#         'require_symbols': False,
#         'forbidden_chars': [],
#         'description': 'Twitter requires strong passwords with mixed case and numbers'
#     },
#     'youtube': {
#         'name': 'YouTube',
#         'min_length': 8,
#         'max_length': 100,
#         'require_uppercase': True,
#         'require_lowercase': True,
#         'require_numbers': True,
#         'require_symbols': True,
#         'forbidden_chars': [],
#         'description': 'YouTube (Google) requires strong passwords with all character types'
#     },
#     'linkedin': {
#         'name': 'LinkedIn',
#         'min_length': 6,
#         'max_length': 200,
#         'require_uppercase': True,
#         'require_lowercase': True,
#         'require_numbers': True,
#         'require_symbols': False,
#         'forbidden_chars': [],
#         'description': 'LinkedIn requires mixed case letters and numbers'
#     },
#     'tiktok': {
#         'name': 'TikTok',
#         'min_length': 8,
#         'max_length': 20,
#         'require_uppercase': True,
#         'require_lowercase': True,
#         'require_numbers': True,
#         'require_symbols': False,
#         'forbidden_chars': [],
#         'description': 'TikTok requires 8-20 characters with mixed case and numbers'
#     },
#     'snapchat': {
#         'name': 'Snapchat',
#         'min_length': 8,
#         'max_length': 50,
#         'require_uppercase': True,
#         'require_lowercase': True,
#         'require_numbers': True,
#         'require_symbols': False,
#         'forbidden_chars': [],
#         'description': 'Snapchat requires strong passwords with mixed case and numbers'
#     },
#     'pinterest': {
#         'name': 'Pinterest',
#         'min_length': 6,
#         'max_length': 100,
#         'require_uppercase': False,
#         'require_lowercase': True,
#         'require_numbers': False,
#         'require_symbols': False,
#         'forbidden_chars': [],
#         'description': 'Pinterest has flexible password requirements'
#     },
#     'reddit': {
#         'name': 'Reddit',
#         'min_length': 8,
#         'max_length': 128,
#         'require_uppercase': True,
#         'require_lowercase': True,
#         'require_numbers': True,
#         'require_symbols': True,
#         'forbidden_chars': [],
#         'description': 'Reddit recommends strong passwords with all character types'
#     },
#     'discord': {
#         'name': 'Discord',
#         'min_length': 6,
#         'max_length': 72,
#         'require_uppercase': False,
#         'require_lowercase': True,
#         'require_numbers': False,
#         'require_symbols': False,
#         'forbidden_chars': [],
#         'description': 'Discord requires minimum 6 characters'
#     },
#     'telegram': {
#         'name': 'Telegram',
#         'min_length': 5,
#         'max_length': 256,
#         'require_uppercase': False,
#         'require_lowercase': True,
#         'require_numbers': False,
#         'require_symbols': False,
#         'forbidden_chars': [],
#         'description': 'Telegram has minimal password requirements'
#     }
# }

# def get_platform_rules(platform_name):
#     """Get rules for a specific platform"""
#     return PLATFORM_RULES.get(platform_name.lower(), None)

# def validate_password_for_platform(password, platform_name):
#     """Validate if password meets platform requirements"""
#     rules = get_platform_rules(platform_name)
#     if not rules:
#         return False, "Platform not found"
    
#     errors = []
    
#     # Check length
#     if len(password) < rules['min_length']:
#         errors.append(f"Password must be at least {rules['min_length']} characters")
#     if len(password) > rules['max_length']:
#         errors.append(f"Password must not exceed {rules['max_length']} characters")
    
#     # Check character requirements
#     if rules['require_uppercase'] and not any(c.isupper() for c in password):
#         errors.append("Password must contain uppercase letters")
    
#     if rules['require_lowercase'] and not any(c.islower() for c in password):
#         errors.append("Password must contain lowercase letters")
    
#     if rules['require_numbers'] and not any(c.isdigit() for c in password):
#         errors.append("Password must contain numbers")
    
#     if rules['require_symbols'] and not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
#         errors.append("Password must contain symbols")
    
#     # Check forbidden characters
#     for char in rules['forbidden_chars']:
#         if char in password:
#             errors.append(f"Password cannot contain '{char}'")
    
#     return len(errors) == 0, errors



"""
High-Security Platform-specific password rules and requirements
All rules designed to ensure 85%+ password strength with maximum security
"""

PLATFORM_RULES = {
    'facebook': {
        'name': 'Facebook',
        'min_length': 14,
        'max_length': 50,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '"', "'"],
        'min_uppercase': 2,
        'min_lowercase': 3,
        'min_numbers': 2,
        'min_symbols': 2,
        'no_sequential': True,
        'no_repetition': True,
        'description': 'Facebook ultra-secure: 14+ chars with all character types, no sequential patterns'
    },
    'instagram': {
        'name': 'Instagram',
        'min_length': 15,
        'max_length': 30,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '\\', '/', '"'],
        'min_uppercase': 2,
        'min_lowercase': 4,
        'min_numbers': 3,
        'min_symbols': 2,
        'no_sequential': True,
        'no_repetition': True,
        'description': 'Instagram maximum security: 15+ chars, mixed case, numbers, symbols mandatory'
    },
    'whatsapp': {
        'name': 'WhatsApp',
        'min_length': 16,
        'max_length': 64,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '\t', '\n'],
        'min_uppercase': 3,
        'min_lowercase': 4,
        'min_numbers': 3,
        'min_symbols': 3,
        'no_sequential': True,
        'no_repetition': True,
        'description': 'WhatsApp enterprise security: 16+ chars with complex character requirements'
    },
    'twitter': {
        'name': 'Twitter/X',
        'min_length': 18,
        'max_length': 50,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '"', "'", '\\'],
        'min_uppercase': 3,
        'min_lowercase': 5,
        'min_numbers': 3,
        'min_symbols': 4,
        'no_sequential': True,
        'no_repetition': True,
        'require_mixed_case_alternation': True,
        'description': 'Twitter/X maximum protection: 18+ chars with advanced security patterns'
    },
    'youtube': {
        'name': 'YouTube',
        'min_length': 20,
        'max_length': 100,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '"', "'", '<', '>', '&'],
        'min_uppercase': 4,
        'min_lowercase': 6,
        'min_numbers': 4,
        'min_symbols': 4,
        'no_sequential': True,
        'no_repetition': True,
        'require_mixed_case_alternation': True,
        'description': 'YouTube ultra-secure: 20+ chars with enterprise-grade security requirements'
    },
    'linkedin': {
        'name': 'LinkedIn',
        'min_length': 16,
        'max_length': 200,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '"', "'", '\\', '/'],
        'min_uppercase': 3,
        'min_lowercase': 5,
        'min_numbers': 3,
        'min_symbols': 3,
        'no_sequential': True,
        'no_repetition': True,
        'require_mixed_case_alternation': True,
        'description': 'LinkedIn professional security: 16+ chars with strict business-grade requirements'
    },
    'tiktok': {
        'name': 'TikTok',
        'min_length': 17,
        'max_length': 25,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '"', "'", '`'],
        'min_uppercase': 3,
        'min_lowercase': 5,
        'min_numbers': 3,
        'min_symbols': 3,
        'no_sequential': True,
        'no_repetition': True,
        'require_mixed_case_alternation': True,
        'description': 'TikTok high security: 17+ chars with advanced pattern protection'
    },
    'snapchat': {
        'name': 'Snapchat',
        'min_length': 15,
        'max_length': 50,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '"', "'", '\\'],
        'min_uppercase': 3,
        'min_lowercase': 4,
        'min_numbers': 3,
        'min_symbols': 3,
        'no_sequential': True,
        'no_repetition': True,
        'require_mixed_case_alternation': True,
        'description': 'Snapchat maximum security: 15+ chars with comprehensive protection rules'
    },
    'pinterest': {
        'name': 'Pinterest',
        'min_length': 14,
        'max_length': 100,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '"', "'", '<', '>'],
        'min_uppercase': 2,
        'min_lowercase': 4,
        'min_numbers': 3,
        'min_symbols': 2,
        'no_sequential': True,
        'no_repetition': True,
        'description': 'Pinterest enhanced security: 14+ chars with strict character mixing'
    },
    'reddit': {
        'name': 'Reddit',
        'min_length': 19,
        'max_length': 128,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '"', "'", '\\', '\t'],
        'min_uppercase': 4,
        'min_lowercase': 6,
        'min_numbers': 4,
        'min_symbols': 4,
        'no_sequential': True,
        'no_repetition': True,
        'require_mixed_case_alternation': True,
        'require_symbol_spread': True,
        'description': 'Reddit ultra-high security: 19+ chars with maximum entropy requirements'
    },
    'discord': {
        'name': 'Discord',
        'min_length': 16,
        'max_length': 72,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '"', "'", '`', '\\'],
        'min_uppercase': 3,
        'min_lowercase': 5,
        'min_numbers': 3,
        'min_symbols': 3,
        'no_sequential': True,
        'no_repetition': True,
        'require_mixed_case_alternation': True,
        'description': 'Discord gaming security: 16+ chars with anti-pattern protection'
    },
    'telegram': {
        'name': 'Telegram',
        'min_length': 18,
        'max_length': 256,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forgotten_chars': [' ', '"', "'", '\\', '\n', '\t'],
        'min_uppercase': 4,
        'min_lowercase': 6,
        'min_numbers': 4,
        'min_symbols': 4,
        'no_sequential': True,
        'no_repetition': True,
        'require_mixed_case_alternation': True,
        'require_symbol_spread': True,
        'description': 'Telegram maximum encryption security: 18+ chars with cryptographic strength'
    },
    'twitch': {
        'name': 'Twitch',
        'min_length': 15,
        'max_length': 60,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '"', "'", '\\', '<', '>'],
        'min_uppercase': 3,
        'min_lowercase': 4,
        'min_numbers': 3,
        'min_symbols': 3,
        'no_sequential': True,
        'no_repetition': True,
        'require_mixed_case_alternation': True,
        'description': 'Twitch streaming security: 15+ chars with content creator protection'
    },
    'spotify': {
        'name': 'Spotify',
        'min_length': 16,
        'max_length': 80,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '"', "'", '\\', '&'],
        'min_uppercase': 3,
        'min_lowercase': 5,
        'min_numbers': 3,
        'min_symbols': 3,
        'no_sequential': True,
        'no_repetition': True,
        'require_mixed_case_alternation': True,
        'description': 'Spotify premium security: 16+ chars with music platform protection'
    },
    'netflix': {
        'name': 'Netflix',
        'min_length': 17,
        'max_length': 70,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '"', "'", '\\', '<', '>', '&'],
        'min_uppercase': 3,
        'min_lowercase': 5,
        'min_numbers': 4,
        'min_symbols': 3,
        'no_sequential': True,
        'no_repetition': True,
        'require_mixed_case_alternation': True,
        'description': 'Netflix streaming security: 17+ chars with entertainment platform protection'
    },
    'amazon': {
        'name': 'Amazon',
        'min_length': 20,
        'max_length': 100,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '"', "'", '\\', '<', '>', '&', '|'],
        'min_uppercase': 4,
        'min_lowercase': 6,
        'min_numbers': 4,
        'min_symbols': 4,
        'no_sequential': True,
        'no_repetition': True,
        'require_mixed_case_alternation': True,
        'require_symbol_spread': True,
        'description': 'Amazon e-commerce maximum security: 20+ chars with financial-grade protection'
    },
    'google': {
        'name': 'Google',
        'min_length': 22,
        'max_length': 100,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '"', "'", '\\', '<', '>', '&', '|', '`'],
        'min_uppercase': 5,
        'min_lowercase': 7,
        'min_numbers': 5,
        'min_symbols': 5,
        'no_sequential': True,
        'no_repetition': True,
        'require_mixed_case_alternation': True,
        'require_symbol_spread': True,
        'require_entropy_minimum': 100,
        'description': 'Google enterprise security: 22+ chars with maximum entropy and security patterns'
    },
    'microsoft': {
        'name': 'Microsoft',
        'min_length': 21,
        'max_length': 120,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '"', "'", '\\', '<', '>', '&', '|', '`', '\t'],
        'min_uppercase': 5,
        'min_lowercase': 6,
        'min_numbers': 5,
        'min_symbols': 5,
        'no_sequential': True,
        'no_repetition': True,
        'require_mixed_case_alternation': True,
        'require_symbol_spread': True,
        'require_entropy_minimum': 95,
        'description': 'Microsoft enterprise security: 21+ chars with corporate-grade protection standards'
    },
    'apple': {
        'name': 'Apple',
        'min_length': 20,
        'max_length': 90,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_numbers': True,
        'require_symbols': True,
        'forbidden_chars': [' ', '"', "'", '\\', '<', '>', '&', '|'],
        'min_uppercase': 4,
        'min_lowercase': 6,
        'min_numbers': 4,
        'min_symbols': 4,
        'no_sequential': True,
        'no_repetition': True,
        'require_mixed_case_alternation': True,
        'require_symbol_spread': True,
        'require_entropy_minimum': 90,
        'description': 'Apple ecosystem security: 20+ chars with premium device protection standards'
    }
}

# Advanced Security Configuration
SECURITY_LEVELS = {
    'maximum': {
        'min_entropy': 90,
        'require_all_char_types': True,
        'min_char_variety': 4,
        'no_dictionary_words': True,
        'no_keyboard_patterns': True,
        'no_date_patterns': True,
        'no_name_patterns': True
    },
    'ultra': {
        'min_entropy': 100,
        'require_all_char_types': True,
        'min_char_variety': 4,
        'no_dictionary_words': True,
        'no_keyboard_patterns': True,
        'no_date_patterns': True,
        'no_name_patterns': True,
        'require_symbol_distribution': True
    }
}

# Extended symbol sets for maximum security
SYMBOL_SETS = {
    'basic': "!@#$%^&*()_+-=[]{}|;:,.<>?",
    'extended': "!@#$%^&*()_+-=[]{}|;:,.<>?~`/\\\"'",
    'maximum': "!@#$%^&*()_+-=[]{}|;:,.<>?~`/\\\"'¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿"
}

# Forbidden patterns for maximum security
FORBIDDEN_PATTERNS = [
    # Sequential patterns
    r'(012|123|234|345|456|567|678|789|890)',
    r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)',
    
    # Keyboard patterns
    r'(qwe|wer|ert|rty|tyu|yui|uio|iop|asd|sdf|dfg|fgh|ghj|hjk|jkl|zxc|xcv|cvb|vbn|bnm)',
    r'(qaz|wsx|edc|rfv|tgb|yhn|ujm|ik|ol|p)',
    
    # Repetition patterns
    r'(.)\1{2,}',  # 3 or more repeated characters
    
    # Common weak patterns
    r'(password|admin|login|user|guest|test|demo|temp)',
    r'(111|000|999|aaa|zzz)',
    
    # Date patterns
    r'(19|20)\d{2}',  # Years
    r'(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])',  # Dates
    
    # Phone patterns
    r'\d{10}',  # 10 digit sequences
    
    # Common substitutions
    r'(p@ssw0rd|p4ssw0rd|passw0rd|4dm1n|@dmin)'
]

def get_platform_rules(platform_name):
    """Get rules for a specific platform with maximum security settings"""
    platform_key = platform_name.lower().strip()
    return PLATFORM_RULES.get(platform_key, None)

def get_security_level(level='maximum'):
    """Get security configuration for specified level"""
    return SECURITY_LEVELS.get(level, SECURITY_LEVELS['maximum'])

def validate_password_for_platform(password, platform_name):
    """
    Validate if password meets ultra-strict platform requirements
    Returns: (is_valid, errors_list, strength_score)
    """
    rules = get_platform_rules(platform_name)
    if not rules:
        return False, ["Platform not found"], 0
    
    errors = []
    strength_bonus = 0
    
    # Check minimum length (critical for 85%+ strength)
    if len(password) < rules['min_length']:
        errors.append(f"Password must be at least {rules['min_length']} characters")
        return False, errors, 0
    
    # Check maximum length
    if len(password) > rules['max_length']:
        errors.append(f"Password must not exceed {rules['max_length']} characters")
    
    # Character type requirements (all mandatory for 85%+ strength)
    uppercase_count = sum(1 for c in password if c.isupper())
    lowercase_count = sum(1 for c in password if c.islower())
    number_count = sum(1 for c in password if c.isdigit())
    symbol_count = sum(1 for c in password if c in SYMBOL_SETS['extended'])
    
    # Check minimum character requirements
    if uppercase_count < rules.get('min_uppercase', 1):
        errors.append(f"Password must contain at least {rules.get('min_uppercase', 1)} uppercase letters")
    
    if lowercase_count < rules.get('min_lowercase', 1):
        errors.append(f"Password must contain at least {rules.get('min_lowercase', 1)} lowercase letters")
    
    if number_count < rules.get('min_numbers', 1):
        errors.append(f"Password must contain at least {rules.get('min_numbers', 1)} numbers")
    
    if symbol_count < rules.get('min_symbols', 1):
        errors.append(f"Password must contain at least {rules.get('min_symbols', 1)} special characters")
    
    # Check forbidden characters
    for char in rules.get('forbidden_chars', []):
        if char in password:
            errors.append(f"Password cannot contain '{char}'")
    
    # Advanced pattern checking for maximum security
    if rules.get('no_sequential', False):
        for pattern in FORBIDDEN_PATTERNS[:3]:  # Sequential patterns
            if __import__('re').search(pattern, password.lower()):
                errors.append("Password cannot contain sequential characters")
                break
    
    if rules.get('no_repetition', False):
        if __import__('re').search(r'(.)\1{2,}', password):
            errors.append("Password cannot contain 3+ repeated characters")
    
    # Mixed case alternation check
    if rules.get('require_mixed_case_alternation', False):
        if not __import__('re').search(r'[a-z][A-Z]|[A-Z][a-z]', password):
            errors.append("Password must have alternating upper and lowercase letters")
    
    # Symbol distribution check
    if rules.get('require_symbol_spread', False) and symbol_count > 0:
        # Check if symbols are distributed throughout password
        symbol_positions = [i for i, c in enumerate(password) if c in SYMBOL_SETS['extended']]
        if symbol_positions:
            distribution_score = len(set(p // (len(password) // 4) for p in symbol_positions))
            if distribution_score < 2:
                errors.append("Special characters must be distributed throughout the password")
    
    # Calculate strength score for validation
    strength_score = calculate_advanced_strength(password, rules)
    
    # Require minimum 85% strength
    if strength_score < 85:
        errors.append(f"Password strength ({strength_score}%) must be at least 85%")
    
    return len(errors) == 0, errors, strength_score

def calculate_advanced_strength(password, rules):
    """
    Calculate password strength with enhanced algorithms for 85%+ targeting
    """
    if not password:
        return 0
    
    score = 0
    
    # Length scoring (enhanced for longer passwords)
    length = len(password)
    if length >= 20:
        score += 30  # Bonus for very long passwords
    elif length >= 16:
        score += 25
    elif length >= 12:
        score += 20
    elif length >= 8:
        score += 10
    else:
        return 0  # Too short for any meaningful score
    
    # Character variety scoring (enhanced requirements)
    has_lower = bool(__import__('re').search(r'[a-z]', password))
    has_upper = bool(__import__('re').search(r'[A-Z]', password))
    has_digit = bool(__import__('re').search(r'\d', password))
    has_symbol = bool(__import__('re').search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password))
    
    # All character types required for high score
    if has_lower and has_upper and has_digit and has_symbol:
        score += 25  # All types present
    else:
        return 0  # Must have all types for 85%+
    
    # Character count bonuses
    char_counts = {
        'upper': sum(1 for c in password if c.isupper()),
        'lower': sum(1 for c in password if c.islower()),
        'digit': sum(1 for c in password if c.isdigit()),
        'symbol': sum(1 for c in password if c in SYMBOL_SETS['basic'])
    }
    
    # Bonus for having minimum required counts
    for char_type, count in char_counts.items():
        min_required = rules.get(f'min_{char_type}s', 1) if char_type != 'upper' else rules.get('min_uppercase', 1)
        if count >= min_required:
            score += 5
    
    # Entropy calculation
    charset_size = 0
    if has_lower: charset_size += 26
    if has_upper: charset_size += 26
    if has_digit: charset_size += 10
    if has_symbol: charset_size += len(SYMBOL_SETS['basic'])
    
    entropy = length * __import__('math').log2(charset_size) if charset_size > 0 else 0
    if entropy >= 80:
        score += 15
    elif entropy >= 60:
        score += 10
    elif entropy >= 40:
        score += 5
    
    # Pattern penalty (strict for high security)
    penalties = 0
    
    # Check for forbidden patterns
    for pattern in FORBIDDEN_PATTERNS:
        if __import__('re').search(pattern, password.lower()):
            penalties += 10
    
    # Dictionary word penalty
    common_words = ['password', 'admin', 'login', 'user', 'welcome', 'secret', 'secure']
    for word in common_words:
        if word in password.lower():
            penalties += 20
    
    # Apply penalties
    score -= penalties
    
    # Bonus for exceptional length and complexity
    if length >= 18 and all([has_lower, has_upper, has_digit, has_symbol]):
        score += 10
    
    if length >= 22:
        score += 5  # Extra bonus for very long passwords
    
    # Ensure score stays within bounds
    score = max(0, min(100, score))
    
    return score

def get_recommended_length_for_platform(platform_name):
    """Get recommended password length to achieve 85%+ strength"""
    rules = get_platform_rules(platform_name)
    if rules:
        # Return a length that ensures 85%+ strength
        return max(rules['min_length'], 16)  # At least 16 for strong passwords
    return 16

def get_platform_difficulty_rating(platform_name):
    """Get difficulty rating for platform (1-10 scale)"""
    rules = get_platform_rules(platform_name)
    if not rules:
        return 5
    
    difficulty = 0
    difficulty += min(rules['min_length'] // 2, 10)  # Length component
    difficulty += rules.get('min_uppercase', 0)
    difficulty += rules.get('min_lowercase', 0)
    difficulty += rules.get('min_numbers', 0)
    difficulty += rules.get('min_symbols', 0)
    
    if rules.get('no_sequential', False): difficulty += 1
    if rules.get('no_repetition', False): difficulty += 1
    if rules.get('require_mixed_case_alternation', False): difficulty += 1
    if rules.get('require_symbol_spread', False): difficulty += 1
    
    return min(difficulty, 10)

# Export list of all supported platforms
SUPPORTED_PLATFORMS = list(PLATFORM_RULES.keys())

# Security recommendations for users
SECURITY_TIPS = [
    "Use unique passwords for each platform",
    "Enable two-factor authentication wherever possible",
    "Store passwords in a reputable password manager",
    "Change passwords every 3-6 months",
    "Never share passwords or write them down",
    "Avoid using personal information in passwords",
    "Use passphrases with random words for easier memorization",
    "Regularly check for data breaches affecting your accounts"
]
