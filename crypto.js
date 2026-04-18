// Intentionally bad crypto — test fixture for Sprint 9 E2E.
const crypto = require('crypto');

// MD5 for password — weak
function hashPassword(pw) {
  return crypto.createHash('md5').update(pw).digest('hex');
}

// Math.random for token — not cryptographically secure
function generateToken() {
  return Math.random().toString(36).substring(2);
}

// DES — deprecated
function legacyEncrypt(data, key) {
  const cipher = crypto.createCipheriv('des-ecb', key, null);
  return Buffer.concat([cipher.update(data), cipher.final()]);
}

module.exports = { hashPassword, generateToken, legacyEncrypt };
