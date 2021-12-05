import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule} from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { AboutComponent } from './about/about.component';
import { ProductComponent } from './product/product.component';
import { HomeComponent } from './home/home.component';
//import { AuthComponent } from './auth/auth.component';
import { AdminComponent } from './admin/admin.component';
import { SignInComponent } from './sign-in/sign-in.component';

@NgModule({
  declarations: [
    //AppComponent, HeaderComponent, FooterComponent, AboutComponent, ProductComponent, HomeComponent, AuthComponent, AdminComponent, SignInComponent
    AppComponent, HeaderComponent, FooterComponent, AboutComponent, ProductComponent, HomeComponent, AdminComponent, SignInComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
