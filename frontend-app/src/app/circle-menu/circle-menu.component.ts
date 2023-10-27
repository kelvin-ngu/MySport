import { Component } from '@angular/core';
import { DynamicComponentLoaderService } from '../dynamic-component-loader.service';
import { Component1Component } from '../component1/component1.component';
import { Component2Component } from '../component2/component2.component';

@Component({
  selector: 'app-circle-menu',
  templateUrl: './circle-menu.component.html',
  styleUrls: ['./circle-menu.component.css']
})
export class CircleMenuComponent {
  constructor(private dynamicComponentLoaderService: DynamicComponentLoaderService) {}

  loadComponent1(): void {
    this.dynamicComponentLoaderService.loadComponent(Component1Component);
  }

  loadComponent2(): void {
    this.dynamicComponentLoaderService.loadComponent(Component2Component);
  }
}

