import {Component, OnInit} from "@angular/core"
import {AuthService} from "../auth.service"

@Component({
    selector: "app-header",
    templateUrl: "./header.component.html",
    styleUrls: ["./header.component.scss"],
})
export class HeaderComponent implements OnInit {
    loggedIn: boolean = false

    constructor(private auth: AuthService) {}

    ngOnInit() {
        this.auth.stateChanges.subscribe((loggedIn) => {
            this.loggedIn = loggedIn
        })
    }
}
