// Intentionally bad crypto — test fixture for Sprint 9 E2E.
package main

import (
	"crypto/des"
	"crypto/md5"
	"crypto/rand"
	"crypto/rsa"
	"fmt"
)

func weakHash(data []byte) string {
	// MD5 for integrity — weak
	h := md5.Sum(data)
	return fmt.Sprintf("%x", h)
}

func smallRSAKey() (*rsa.PrivateKey, error) {
	// RSA-1024 — too small
	return rsa.GenerateKey(rand.Reader, 1024)
}

func legacyEncrypt(data, key []byte) ([]byte, error) {
	// DES — deprecated
	block, err := des.NewCipher(key)
	if err != nil {
		return nil, err
	}
	out := make([]byte, len(data))
	block.Encrypt(out, data)
	return out, nil
}
