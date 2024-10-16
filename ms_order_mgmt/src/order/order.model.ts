import { Prisma } from "@prisma/client";

export class Order implements Prisma.OrderCreateInput {
    id?: string;
    customerID: string;
    orderID: string;
    status: string;
}