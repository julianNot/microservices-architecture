package models

type User struct {
	ID         uint   `json:"id" gorm:"primaryKey; autoIncrement"`
	CustomerID int64  `json:"customer_id" gorm:"not null;varchar(20)"`
	Password   string `json:"password" gorm:"not null"`
}
