export interface Device {
    readonly id: number
    readonly name: string
    readonly description: string
}

export interface NewDevice extends Device {
    aws: {
        readonly endpointAddress: string
        readonly certificateArn: string
        readonly certificateId: string
        readonly certificatePem: string
        readonly keyPair: {PublicKey: string; PrivateKey: string}
    }
}
