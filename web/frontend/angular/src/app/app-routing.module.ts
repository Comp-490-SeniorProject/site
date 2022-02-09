import {NgModule} from "@angular/core"
import {RouterModule, Routes} from "@angular/router"

import {AboutComponent} from "./about/about.component"
import {FooterComponent} from "./footer/footer.component"
import {HeaderComponent} from "./header/header.component"
import {HomeComponent} from "./home/home.component"
import {ProductComponent} from "./product/product.component"
import {SignInComponent} from "./sign-in/sign-in.component"

import {AdminComponent} from "./admin/admin.component"
//import { AuthComponent } from './auth/auth.component';
import {AuthGuard} from "./auth.guard"
import { SignUpComponent } from "./sign-up/sign-up.component"
const routes: Routes = [
    {path: "", pathMatch: "full", component: HomeComponent},
    {path: "app-header", component: HeaderComponent},
    {path: "app-footer", component: FooterComponent},
    {path: "app-about", component: AboutComponent},
    {path: "app-product", component: ProductComponent},
    {path: "app-home", component: HomeComponent},
    //{ path: 'app-auth',
    //component: AuthComponent},
    {path: "app-admin", component: AdminComponent, canActivate: [AuthGuard]},
    {path: "app-sign-in", component: SignInComponent},
    {path: "app-sign-up", component: SignUpComponent},
]

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule],
})
export class AppRoutingModule {}
