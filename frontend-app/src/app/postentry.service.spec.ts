import { TestBed } from '@angular/core/testing';

import { PostentryService } from './postentry.service';

describe('PostentryService', () => {
  let service: PostentryService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PostentryService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
