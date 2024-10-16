import { Injectable } from '@nestjs/common';
import { Order, Prisma } from '@prisma/client';
import { PrismaService } from 'src/prisma/prisma.service';

@Injectable()
export class OrderService {
    
    constructor(private prismaService: PrismaService){}

    async createOrder(data: Prisma.OrderCreateInput): Promise<Prisma.OrderCreateInput | any> {
        const newOrder: Order | any = await this.prismaService.order.create({
            data
        })
        return newOrder;
    }

    async updateOrderStatus(orderId: string, status:string): Promise<any> {
        const order: Order = await this.prismaService.order.findFirstOrThrow({
            where:{orderID:orderId}
        })
        return await this.prismaService.order.update({ 
            where:{id:order.id},
            data:{
                status: status
            }
        })
    }

    async findOrderByCustomerId(customerId:string): Promise<Order> {
        const order: Order = await this.prismaService.order.findFirstOrThrow({
            where:{customerID:customerId}
        })
        return order;
    }

}
