import { Injectable, ComponentFactoryResolver, Injector, ApplicationRef, EmbeddedViewRef, ComponentRef } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DynamicComponentLoaderService {
  constructor(
    private componentFactoryResolver: ComponentFactoryResolver,
    private injector: Injector,
    private appRef: ApplicationRef
  ) {}

  private componentRef!: ComponentRef<any>;

  loadComponent(component: any): void {
    // Create a factory for the component.
    const factory = this.componentFactoryResolver.resolveComponentFactory(component);

    // Create a component and attach it to the application view.
    this.componentRef = factory.create(this.injector);

    // Attach the component to the DOM.
    this.appRef.attachView(this.componentRef.hostView);

    // Append the component to a container (e.g., a div in your template).
    document.body.appendChild((this.componentRef.hostView as EmbeddedViewRef<any>).rootNodes[0]);
  }

  unloadComponent(): void {
    // Check if a component is loaded and then destroy it.
    if (this.componentRef) {
      this.appRef.detachView(this.componentRef.hostView);
      this.componentRef.destroy();
    }
  }
}