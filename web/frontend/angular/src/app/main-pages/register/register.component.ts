import {Component, OnInit} from "@angular/core"
import { FormGroup } from "@angular/forms"
import { Validators } from "@angular/forms"
import { FormBuilder } from "@angular/forms"
import { Router } from "@angular/router"
import { AuthService } from "src/app/auth/auth.service"

@Component({
    selector: "app-register",
    templateUrl: "./register.component.html",
    styleUrls: ["./register.component.scss"],
})
export class RegisterComponent implements OnInit {
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

    register() {
        this.isSubmitted = true
        if (this.authForm.invalid) {
            return
        }
        this.authService.register(this.authForm.value)
        this.router.navigateByUrl("homepage")
    }
}
