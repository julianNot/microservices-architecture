package main

import (
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
	"microservices-architecture.com/database"
	"github.com/joho/godotenv"
	"microservices-architecture.com/routes"
)

func main() {
	r := gin.Default()
	if err := godotenv.Load(); err != nil {
		log.Fatalf("Error cargando archivo .env: %v", err)
	}
	database.Init()
	routes.InitRoutes((r))

	r.GET("/", func(ctx *gin.Context) {
		ctx.JSON(http.StatusOK, gin.H{"data": "Welcome"})
	})

	if err := r.Run(); err != nil {
		log.Fatalf("Error al iniciar el servidor: %v", err)
	}
}
