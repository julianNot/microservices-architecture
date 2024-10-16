import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { PrismaService } from './prisma/prisma.service';
import { OrderModule } from './order/order.module';

@Module({
  imports: [OrderModule],
  controllers: [AppController],
  providers: [AppService, PrismaService],
})
export class AppModule {}
