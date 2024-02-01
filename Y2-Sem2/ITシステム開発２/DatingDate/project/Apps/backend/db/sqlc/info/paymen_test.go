package db

import (
	"context"
	"testing"

	"github.com/brianvoe/gofakeit/v6"
	"github.com/google/uuid"
	"github.com/stretchr/testify/require"
)

func TestCreatePayment(t *testing.T) {
	user := CreateRandomUserFixInformaion(t)
	CreateRandomPayment(t, user)
}

func CreateRandomPayment(t *testing.T, user Fixinformation) Payment {
	id, _ := uuid.NewRandom()
	arg := CreatePaymentParams{
		PayID:       id,
		Fullname:    user.FirstName + user.LastName,
		PaymentType: gofakeit.CreditCardType(),
		Amount:      int32(gofakeit.Price(2000, 4000)),
		Product:     "ターゲット",
	}

	Pay, err := testinfoQueries.CreatePayment(context.Background(), arg)
	require.NoError(t, err)
	require.NotEmpty(t, Pay)
	require.Equal(t, Pay.PayID, arg.PayID)
	require.Equal(t, Pay.Fullname, arg.Fullname)
	require.Equal(t, Pay.PaymentType, arg.PaymentType)
	require.Equal(t, Pay.Amount, arg.Amount)
	require.Equal(t, Pay.Product, arg.Product)

	require.NotEmpty(t, Pay.PayID)
	require.NotEmpty(t, Pay.PayAt)

	return Pay
}

func TestGetPayment(t *testing.T) {
	user := CreateRandomUserFixInformaion(t)
	pay := CreateRandomPayment(t, user)

	GetP, err := testinfoQueries.GetPayment(context.Background(), pay.PayID)
	require.NoError(t, err)
	require.NotEmpty(t, GetP)
}
