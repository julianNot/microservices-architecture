package routes

import (
	"microservices-architecture.com/controllers"

	"github.com/gin-gonic/gin"
)

func InitRoutes(r *gin.Engine) {
	authGroup := r.Group("/login")
	{
		authGroup.POST("/createuser", controllers.CreateUser)
		authGroup.POST("/authuser", controllers.AuthUser)
	}
}