import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { DashboardLayoutComponent } from './layouts/dashboard-layout/dashboard-layout.component';
import { DevicesLayoutComponent } from './layouts/devices-layout/devices-layout.component';
import { MainLayoutComponent } from './layouts/main-layout/main-layout.component';
import { SettingsLayoutComponent } from './layouts/settings-layout/settings-layout.component';

import { NotificationsComponent } from './dashboard-pages/notifications/notifications.component';
import { ParametersComponent } from './dashboard-pages/parameters/parameters.component';
import { DataLogComponent } from './dashboard-pages/parameters/data-log/data-log.component';
import { RuntestsComponent } from './dashboard-pages/runtests/runtests.component';
import { ScheduleComponent } from './dashboard-pages/schedule/schedule.component';
import { SummaryComponent } from './dashboard-pages/summary/summary.component';

import { DeviceOverviewComponent } from './devices-pages/device-overview/device-overview.component';
import { ManageDevicesComponent } from './devices-pages/manage-devices/manage-devices.component';

//import { AboutComponent } from './main-pages/about/about.component';
import { AuthGuard } from './auth/auth.guard';
import { AdminComponent } from './main-pages/admin/admin.component';
import { HomeComponent } from './main-pages/home/home.component';
//import { ProductComponent } from './main-pages/product/product.component';
import { RegisterComponent } from './main-pages/register/register.component';
import { SignInComponent } from './main-pages/sign-in/sign-in.component';
import { AccountSettingsComponent } from './settings-pages/account-settings/account-settings.component';

import { PageNotFoundComponent } from './page-not-found/page-not-found.component';

const routes: Routes = [

  // Main layout pages: Home, About, Product, Sign In, Register, Admin
  // "Page Not Found" page also uses this layout with the same header and footer.
  {
    path: '',
    component: MainLayoutComponent,
    children: [
      {
        path: '', component: HomeComponent, pathMatch: 'full'
      },
      //{
        //path: 'about', component: AboutComponent
      //},
      //{
        //path: 'product', component: ProductComponent
      //},
      {
        path: 'register', component: RegisterComponent
      },
      {
        path: 'sign-in', component: SignInComponent
      },
      {
        path: 'admin', component: AdminComponent, canActivate: [AuthGuard]
      },
      // Redirect to "page not found" for routes/url's that don't exist at all in the whole site.
      // Useful when testing certain functionality to make sure a feature routes to the correct page
      // or performs the expected behavior.
      {
        path: 'error-404', component: PageNotFoundComponent
      }
    ]
  },

  // Devices layout pages: Device Overview, Manage Devices
  {
    path: '',
    component: DevicesLayoutComponent,
    children: [
      {
        path: 'my-devices', component: DeviceOverviewComponent
      },
      {
        path: 'manage-devices', component: ManageDevicesComponent
      }
    ]
  },

  // Dashboard layout pages: Summary, Parameters, Data Log, Run Tests, Schedule, Notifications
  {
    path: '',
    component: DashboardLayoutComponent,
    children: [
      {
        path: 'my-devices/device-name/summary', component: SummaryComponent
      },
      {
        path: 'my-devices/device-name/parameters', component: ParametersComponent
      },
      {
        path: 'my-devices/device-name/parameters/data-log', component: DataLogComponent
      },
      {
        path: 'my-devices/device-name/run-tests', component: RuntestsComponent
      },
      {
        path: 'my-devices/device-name/schedule', component: ScheduleComponent
      },
      {
        path: 'my-devices/device-name/notifications', component: NotificationsComponent
      }
    ]
  },

  // Settings layout pages: Account
  {
    path: '',
    component: SettingsLayoutComponent,
    children: [
      {
        path: 'settings/account', component: AccountSettingsComponent
      }
    ]
  },

  // Redirect to "page not found" for routes/url's that don't exist at all in the whole site.
  // Useful when testing certain functionality to make sure a feature routes to the correct page
  // or performs the expected behavior.
  {
    path: '**', redirectTo: '/error-404'
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
