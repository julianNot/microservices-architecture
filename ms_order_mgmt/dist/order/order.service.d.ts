import { Order, Prisma } from '@prisma/client';
import { PrismaService } from 'src/prisma/prisma.service';
export declare class OrderService {
    private prismaService;
    constructor(prismaService: PrismaService);
    createOrder(data: Prisma.OrderCreateInput): Promise<Prisma.OrderCreateInput | any>;
    updateOrderStatus(orderId: string, status: string): Promise<any>;
    findOrderByCustomerId(customerId: string): Promise<Order>;
}
