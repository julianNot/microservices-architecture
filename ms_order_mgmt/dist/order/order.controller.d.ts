import { OrderService } from './order.service';
import { Order } from '@prisma/client';
export declare class OrderController {
    private readonly orderService;
    constructor(orderService: OrderService);
    createOrder(order: Order): Promise<Order | any>;
    updateProduct(orderStatus: {
        orderID: string;
        status: string;
    }): Promise<Order | any>;
    findOrderByCustomerId(idCustomer: string): Promise<Order | any>;
}
