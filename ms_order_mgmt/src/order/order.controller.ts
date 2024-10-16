import { Body, Controller, Get, Param, Post, Put } from '@nestjs/common';
import { OrderService } from './order.service';
import { Order } from './order.model';

@Controller('order')
export class OrderController {

    constructor(private readonly orderService: OrderService) {}

    @Post('createorder')
    async createOrder(@Body() order: Order): Promise<Order | any>{
        try {
            return await this.orderService.createOrder(order);
        } catch (error) {
            console.log('el error:', error);
            return {status:'error',code:error.code, detail:'Error al crear' ,message: 'Ocurrió un error al crear la orden.'}
        }
    }

    @Put('updateorderstatus')
    async updateProduct(@Body() orderStatus: {orderID:string, status:string}): Promise< Order | any> {
        try {
            return await this.orderService.updateOrderStatus(orderStatus.orderID, orderStatus.status);
        } catch (error) {
            console.log('el error:', error);
            return {status:'error',code:error.code, detail:'Error al crear' ,message: 'Ocurrió un error al crear el usuario.'}
        }
    }

    @Get('findorderbycustomerid/:idcustomer')
    async findOrderByCustomerId(@Param('idcustomer') idCustomer: string): Promise<Order | any> {
        return this.orderService.findOrderByCustomerId(idCustomer);
    }
}
