package controllers

import (
	"net/http"
	"os"
	"time"

	"github.com/dgrijalva/jwt-go"
	"github.com/gin-gonic/gin"
	"golang.org/x/crypto/bcrypt"
	"microservices-architecture.com/database"
	"microservices-architecture.com/models"
)

type Claims struct {
	CustomerID int64 `json:"customer_id"`
	jwt.StandardClaims
}

func AuthUser(ctx *gin.Context) {
	secretKey := os.Getenv("DB_HOST")

	var user models.User

	if err := ctx.ShouldBindJSON(&user); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	var storedUser models.User

	if err := database.DB.Where("customer_id = ?", user.CustomerID).First(&storedUser).Error; err != nil {
		ctx.JSON(http.StatusUnauthorized, gin.H{"error": "Credenciales inválidas"})
		return
	}

	if err := bcrypt.CompareHashAndPassword([]byte(storedUser.Password), []byte(user.Password)); err != nil {
		ctx.JSON(http.StatusUnauthorized, gin.H{"error": "Credenciales inválidas"})
		return
	}

	token := jwt.NewWithClaims(jwt.SigningMethodHS256, &Claims{
		CustomerID: user.CustomerID,
		StandardClaims: jwt.StandardClaims{
			ExpiresAt: time.Now().Add(24 * time.Hour).Unix(),
		},
	})

	tokenString, err := token.SignedString([]byte(secretKey))
	if err != nil {
		ctx.JSON(http.StatusInternalServerError, gin.H{"error": "No se pudo generar el token"})
		return
	}

	ctx.JSON(http.StatusOK, gin.H{"token": tokenString})
}