// Password Generator JavaScript
class PasswordGenerator {
    constructor() {
        this.currentPassword = '';
        this.currentStrength = {};
        this.platformRules = {};
        this.initializeApp();
    }

    async initializeApp() {
        await this.loadPlatformRules();
        this.setupEventListeners();
        this.loadUserPreferences();
    }

    async loadPlatformRules() {
        try {
            const response = await fetch('/api/platforms');
            const data = await response.json();
            this.platformRules = data.platforms;
        } catch (error) {
            console.error('Failed to load platform rules:', error);
            this.showToast('Failed to load platform data', 'error');
        }
    }

    setupEventListeners() {
        // Platform selection change
        document.getElementById('platform').addEventListener('change', () => {
            this.updatePlatformRules();
        });

        // Real-time password strength checking
        document.getElementById('generatedPassword').addEventListener('input', (e) => {
            if (e.target.value) {
                this.checkPasswordStrength(e.target.value);
            }
        });

        // Form validation
        ['uppercase', 'lowercase', 'numbers', 'symbols'].forEach(id => {
            document.getElementById(id).addEventListener('change', this.validateForm);
        });
    }

    updatePlatformRules() {
        const platform = document.getElementById('platform').value;
        const customRules = document.getElementById('customRules');
        const platformRules = document.getElementById('platformRules');
        const platformDescription = document.getElementById('platformDescription');

        if (platform === 'custom') {
            customRules.style.display = 'block';
            platformRules.style.display = 'none';
            platformDescription.textContent = 'Configure custom password requirements';
        } else {
            customRules.style.display = 'none';
            platformRules.style.display = 'block';
            
            const rules = this.platformRules[platform];
            if (rules) {
                platformDescription.textContent = rules.description;
                document.getElementById('rulesContent').innerHTML = this.formatPlatformRules(rules);
            }
        }
    }

    formatPlatformRules(rules) {
        let html = `<strong>${rules.name} Requirements:</strong><br>`;
        html += `• Length: ${rules.min_length}-${rules.max_length} characters<br>`;
        
        const requirements = [];
        if (rules.require_lowercase) requirements.push('Lowercase letters');
        if (rules.require_uppercase) requirements.push('Uppercase letters');
        if (rules.require_numbers) requirements.push('Numbers');
        if (rules.require_symbols) requirements.push('Special characters');
        
        if (requirements.length > 0) {
            html += '• Required: ' + requirements.join(', ');
        } else {
            html += '• Flexible character requirements';
        }
        
        return html;
    }

    async generatePassword() {
        const generateBtn = document.querySelector('button[onclick="generatePassword()"]');
        generateBtn.classList.add('loading');
        generateBtn.disabled = true;

        try {
            const platform = document.getElementById('platform').value;
            const requestData = {
                platform: platform,
                length: parseInt(document.getElementById('lengthRange').value),
                uppercase: document.getElementById('uppercase').checked,
                lowercase: document.getElementById('lowercase').checked,
                numbers: document.getElementById('numbers').checked,
                symbols: document.getElementById('symbols').checked,
                difficulty: document.getElementById('difficulty').value
            };

            const response = await fetch('/api/generate-password', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
                },
                body: JSON.stringify(requestData)
            });

            const data = await response.json();

            if (data.success) {
                this.currentPassword = data.password;
                this.currentStrength = data.strength;
                this.displayPassword(data);
                this.showToast('Password generated successfully!', 'success');
            } else {
                this.showToast(data.error || 'Failed to generate password', 'error');
            }
        } catch (error) {
            console.error('Password generation failed:', error);
            this.showToast('Network error occurred', 'error');
        } finally {
            generateBtn.classList.remove('loading');
            generateBtn.disabled = false;
        }
    }

    displayPassword(data) {
        const resultsDiv = document.getElementById('passwordResults');
        const passwordInput = document.getElementById('generatedPassword');
        
        // Show results section
        resultsDiv.style.display = 'block';
        resultsDiv.classList.add('fade-in');
        
        // Set password
        passwordInput.value = data.password;
        
        // Update strength meter
        this.updateStrengthMeter(data.strength);
        
        // Update details
        this.updatePasswordDetails(data);
        
        // Scroll to results
        resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    updateStrengthMeter(strength) {
        const strengthBar = document.getElementById('strengthBar');
        const strengthText = document.getElementById('strengthText');
        const strengthFeedback = document.getElementById('strengthFeedback');
        
        strengthBar.style.width = strength.score + '%';
        strengthText.textContent = strength.level + ' (' + strength.score + '%)';
        strengthBar.style.backgroundColor = strength.color;
        
        // Update strength class
        strengthBar.className = 'progress-bar strength-' + strength.level.toLowerCase().replace(' ', '-');
        
        // Update feedback
        if (strength.feedback && strength.feedback.length > 0) {
            strengthFeedback.innerHTML = '<strong>Suggestions:</strong><br>' + 
                strength.feedback.map(f => '• ' + f).join('<br>');
        } else {
            strengthFeedback.innerHTML = '<span class="text-success"><i class="fas fa-check"></i> Excellent password strength!</span>';
        }
    }

    updatePasswordDetails(data) {
        const detailsDiv = document.getElementById('passwordDetails');
        const securityDiv = document.getElementById('securityInfo');
        
        detailsDiv.innerHTML = `
            <small class="text-muted">
                <strong>Length:</strong> ${data.password.length} characters<br>
                <strong>Platform:</strong> ${document.getElementById('platform').value.charAt(0).toUpperCase() + document.getElementById('platform').value.slice(1)}<br>
                <strong>Rules:</strong> ${data.rules_applied.join(', ')}
            </small>
        `;
        
        securityDiv.innerHTML = `
            <small class="text-muted">
                <strong>Entropy:</strong> ${data.entropy} bits<br>
                <strong>Generated:</strong> ${new Date().toLocaleString()}<br>
                <strong>Status:</strong> <span class="text-success">Secure</span>
            </small>
        `;
    }

    async checkPasswordStrength(password) {
        try {
            const response = await fetch('/api/check-strength', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
                },
                body: JSON.stringify({ password: password })
            });

            const data = await response.json();
            if (data.success) {
                this.updateStrengthMeter(data.strength);
            }
        } catch (error) {
            console.error('Strength check failed:', error);
        }
    }

    togglePasswordVisibility() {
        const passwordInput = document.getElementById('generatedPassword');
        const eyeIcon = document.getElementById('eyeIcon');
        
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            passwordInput.classList.add('password-visible');
            eyeIcon.className = 'fas fa-eye-slash';
        } else {
            passwordInput.type = 'password';
            passwordInput.classList.remove('password-visible');
            eyeIcon.className = 'fas fa-eye';
        }
    }

    async copyPassword() {
        const passwordInput = document.getElementById('generatedPassword');
        
        try {
            await navigator.clipboard.writeText(passwordInput.value);
            this.showToast('Password copied to clipboard!', 'success');
            
            // Visual feedback
            const copyBtn = event.target.closest('button');
            const originalHTML = copyBtn.innerHTML;
            copyBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
            copyBtn.classList.add('btn-success');
            copyBtn.classList.remove('btn-primary');
            
            setTimeout(() => {
                copyBtn.innerHTML = originalHTML;
                copyBtn.classList.remove('btn-success');
                copyBtn.classList.add('btn-primary');
            }, 2000);
            
        } catch (error) {
            // Fallback for older browsers
            passwordInput.select();
            document.execCommand('copy');
            this.showToast('Password copied to clipboard!', 'success');
        }
    }

    async downloadPDF() {
        if (!this.currentPassword) {
            this.showToast('Please generate a password first', 'warning');
            return;
        }

        const downloadBtn = event.target.closest('button');
        downloadBtn.classList.add('loading');
        downloadBtn.disabled = true;

        try {
            const platform = document.getElementById('platform').value;
            const requestData = {
                password: this.currentPassword,
                platform: platform,
                rules: this.getCurrentRules(),
                strength: this.currentStrength,
                entropy: this.calculateEntropy(this.currentPassword)
            };

            const response = await fetch('/api/download-pdf', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
                },
                body: JSON.stringify(requestData)
            });

            if (response.ok) {
                const blob = await response.blob();
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `password_report_${new Date().toISOString().slice(0, 19).replace(/:/g, '-')}.pdf`;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                window.URL.revokeObjectURL(url);
                
                this.showToast('PDF downloaded successfully!', 'success');
            } else {
                throw new Error('Download failed');
            }
        } catch (error) {
            console.error('PDF download failed:', error);
            this.showToast('Failed to download PDF', 'error');
        } finally {
            downloadBtn.classList.remove('loading');
            downloadBtn.disabled = false;
        }
    }

    getCurrentRules() {
        const platform = document.getElementById('platform').value;
        if (platform !== 'custom') {
            const rules = this.platformRules[platform];
            const applied = [`${this.currentPassword.length} characters`];
            if (rules?.require_uppercase) applied.push('Uppercase letters');
            if (rules?.require_lowercase) applied.push('Lowercase letters');
            if (rules?.require_numbers) applied.push('Numbers');
            if (rules?.require_symbols) applied.push('Special characters');
            return applied;
        } else {
            const applied = [`${this.currentPassword.length} characters`];
            if (document.getElementById('uppercase').checked) applied.push('Uppercase letters');
            if (document.getElementById('lowercase').checked) applied.push('Lowercase letters');
            if (document.getElementById('numbers').checked) applied.push('Numbers');
            if (document.getElementById('symbols').checked) applied.push('Special characters');
            return applied;
        }
    }

    calculateEntropy(password) {
        if (!password) return 0;
        
        let charsetSize = 0;
        if (/[a-z]/.test(password)) charsetSize += 26;
        if (/[A-Z]/.test(password)) charsetSize += 26;
        if (/[0-9]/.test(password)) charsetSize += 10;
        if (/[^a-zA-Z0-9]/.test(password)) charsetSize += 32;
        
        return Math.round(password.length * Math.log2(charsetSize) * 100) / 100;
    }

    validateForm() {
        const checkboxes = ['uppercase', 'lowercase', 'numbers', 'symbols'];
        const anyChecked = checkboxes.some(id => document.getElementById(id).checked);
        
        const generateBtn = document.querySelector('button[onclick="generatePassword()"]');
        generateBtn.disabled = !anyChecked;
        
        if (!anyChecked) {
            this.showToast('Please select at least one character type', 'warning');
        }
    }

    showToast(message, type = 'info') {
        const toast = document.getElementById('toast');
        const toastBody = document.getElementById('toastBody');
        const toastHeader = toast.querySelector('.toast-header');
        
        // Set message
        toastBody.textContent = message;
        
        // Set color based on type
        toast.className = `toast toast-${type}`;
        
        // Show toast
        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();
    }

    updateLengthValue(value) {
        document.getElementById('lengthValue').textContent = value;
    }

    loadUserPreferences() {
        try {
            const prefs = JSON.parse(localStorage.getItem('passwordGenPrefs') || '{}');
            
            if (prefs.platform) {
                document.getElementById('platform').value = prefs.platform;
                this.updatePlatformRules();
            }
            
            if (prefs.length) {
                document.getElementById('lengthRange').value = prefs.length;
                this.updateLengthValue(prefs.length);
            }
            
            if (prefs.difficulty) {
                document.getElementById('difficulty').value = prefs.difficulty;
            }
        } catch (error) {
            console.error('Failed to load preferences:', error);
        }
    }

    saveUserPreferences() {
        try {
            const prefs = {
                platform: document.getElementById('platform').value,
                length: document.getElementById('lengthRange').value,
                difficulty: document.getElementById('difficulty').value,
                lastUsed: new Date().toISOString()
            };
            
            localStorage.setItem('passwordGenPrefs', JSON.stringify(prefs));
        } catch (error) {
            console.error('Failed to save preferences:', error);
        }
    }
}

// Global functions for HTML onclick events
let passwordGen;

function updatePlatformRules() {
    passwordGen.updatePlatformRules();
}

function updateLengthValue(value) {
    passwordGen.updateLengthValue(value);
}

function generatePassword() {
    passwordGen.generatePassword();
    passwordGen.saveUserPreferences();
}

function togglePasswordVisibility() {
    passwordGen.togglePasswordVisibility();
}

function copyPassword() {
    passwordGen.copyPassword();
}

function downloadPDF() {
    passwordGen.downloadPDF();
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    passwordGen = new PasswordGenerator();
});

// Add some utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Auto-save form data
setInterval(() => {
    if (passwordGen) {
        passwordGen.saveUserPreferences();
    }
}, 30000); // Save every 30 seconds
