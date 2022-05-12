import {NgModule} from "@angular/core"
import {BrowserModule} from "@angular/platform-browser"
import {FormsModule, ReactiveFormsModule} from "@angular/forms"
import {AppRoutingModule} from "./app-routing.module"
import {HttpClientModule} from "@angular/common/http"

import {AppComponent} from "./app.component"
import {DashboardLayoutComponent} from "./layouts/dashboard-layout/dashboard-layout.component"
import {DevicesLayoutComponent} from "./layouts/devices-layout/devices-layout.component"
import {MainLayoutComponent} from "./layouts/main-layout/main-layout.component"
import {SettingsLayoutComponent} from "./layouts/settings-layout/settings-layout.component"

import {DashboardHeaderComponent} from "./layouts/shared/dashboard-header/dashboard-header.component"
import {DashboardSidebarComponent} from "./layouts/shared/dashboard-sidebar/dashboard-sidebar.component"
import {DevicesSidebarComponent} from "./layouts/shared/devices-sidebar/devices-sidebar.component"
import {GlobalFooterComponent} from "./layouts/shared/global-footer/global-footer.component"
import {MainHeaderComponent} from "./layouts/shared/main-header/main-header.component"
import {SettingsSidebarComponent} from "./layouts/shared/settings-sidebar/settings-sidebar.component"

import {NotificationsComponent} from "./dashboard-pages/notifications/notifications.component"
import {ParametersComponent} from "./dashboard-pages/parameters/parameters.component"
import {RuntestsComponent} from "./dashboard-pages/runtests/runtests.component"
import {ScheduleComponent} from "./dashboard-pages/schedule/schedule.component"
import {SummaryComponent} from "./dashboard-pages/summary/summary.component"

import {DeviceOverviewComponent} from "./devices-pages/device-overview/device-overview.component"
import {ManageDevicesComponent} from "./devices-pages/manage-devices/manage-devices.component"
import {DeviceInfoModalContent} from "./devices-pages/manage-devices/device-info.component"

import {HomeComponent} from "./main-pages/home/home.component"

import {RegisterComponent} from "./main-pages/register/register.component"
import {SignInComponent} from "./main-pages/sign-in/sign-in.component"

import {AccountSettingsComponent} from "./settings-pages/account-settings/account-settings.component"

import {PageNotFoundComponent} from "./page-not-found/page-not-found.component"
import {DataLogComponent} from "./dashboard-pages/parameters/data-log/data-log.component"

import "bootstrap"
import {DevicesHeaderComponent} from "./layouts/shared/devices-header/devices-header.component"
import {SettingsHeaderComponent} from "./layouts/shared/settings-header/settings-header.component"

import {HashLocationStrategy} from "@angular/common"
import {LocationStrategy} from "@angular/common"

import {HttpClientXsrfModule} from "@angular/common/http"
import {NgbModule} from "@ng-bootstrap/ng-bootstrap"

@NgModule({
    declarations: [
        AppComponent,
        DashboardLayoutComponent,
        DevicesLayoutComponent,
        MainLayoutComponent,
        SettingsLayoutComponent,
        DashboardHeaderComponent,
        DashboardSidebarComponent,
        DevicesSidebarComponent,
        GlobalFooterComponent,
        MainHeaderComponent,
        SettingsSidebarComponent,
        NotificationsComponent,
        ParametersComponent,
        RuntestsComponent,
        ScheduleComponent,
        SummaryComponent,
        DeviceOverviewComponent,
        ManageDevicesComponent,
        DeviceInfoModalContent,
        HomeComponent,
        RegisterComponent,
        SignInComponent,
        AccountSettingsComponent,
        DataLogComponent,
        PageNotFoundComponent,
        DevicesHeaderComponent,
        SettingsHeaderComponent,
    ],

    imports: [
        BrowserModule,
        AppRoutingModule,
        NgbModule,
        FormsModule,
        ReactiveFormsModule,
        HttpClientModule,
        HttpClientXsrfModule.withOptions({
            cookieName: "csrftoken",
            headerName: "X-CSRFToken",
        }),
    ],

    providers: [{provide: LocationStrategy, useClass: HashLocationStrategy}],

    bootstrap: [AppComponent],
})
export class AppModule {}
