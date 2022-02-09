import {Component, OnInit} from "@angular/core"
import {FormBuilder, FormGroup, Validators} from "@angular/forms"
import {Router} from "@angular/router"
import {AuthService} from "../auth.service"

@Component({
    selector: "app-sign-in",
    templateUrl: "./sign-in.component.html",
    styleUrls: ["./sign-in.component.scss"],
})
export class SignInComponent implements OnInit {
    constructor(
        private authService: AuthService,
        private router: Router,
        private formBuilder: FormBuilder
    ) {}

    authForm!: FormGroup
    isSubmitted = false

    ngOnInit() {
        this.authForm = this.formBuilder.group({
            email: ["", Validators.required],
            password: ["", Validators.required],
        })
    }

    get formControls() {
        return this.authForm.controls
    }

    async signIn() {
        this.isSubmitted = true
        if (this.authForm.invalid) {
            return
        }

        try {
            await this.authService.signIn(this.authForm.value)
            this.router.navigateByUrl("/admin")
        } catch (ex) {
            alert(`Sign-in failed! ${ex}`)
        }
    }
}
